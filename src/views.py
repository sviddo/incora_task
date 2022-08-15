import json
import jwt
import datetime
from rest_framework.decorators import api_view
from .serializers import UserSerializer
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.hashers import check_password
from .models import User
from .services import get_user_data, CustomException


@api_view(['POST'])
def create_user(request):
    user_serializer = UserSerializer(data=json.loads(request.body))
    if user_serializer.is_valid():
        user_serializer.save()
        return Response("User has been successfully created!", status=status.HTTP_201_CREATED)
    else:
        return Response(user_serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)


@api_view(['POST'])
def login(request):
    login_data = json.loads(request.body)
    if 'email' not in login_data:
        return Response("You have to provide email to log in!", status=status.HTTP_403_FORBIDDEN)
    elif 'password' not in login_data:
        return Response("You have to provide password to log in!", status=status.HTTP_403_FORBIDDEN)

    try:
        user = User.objects.filter(email=login_data['email']).first()
        if not user:
            raise CustomException("Please, provide valid credentials to log in!")
    
        if check_password(login_data['password'], user.password):
            payload = {
                "email": login_data['email'],
                "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
                "iat": datetime.datetime.utcnow()
            }

            token = jwt.encode(payload, 'secret', algorithm='HS256').decode('utf-8')

            response = Response("You have successfully logged in!", status=status.HTTP_200_OK)
            response.set_cookie(key='jwt', value=token, httponly=True)

            return response
        
        raise CustomException("Please, provide valid credentials to log in!")

    except CustomException as exc:
        return Response(str(exc), status=status.HTTP_403_FORBIDDEN)


@api_view(['GET'])
def get_user(request, id: int):
    user = User.objects.filter(pk=id).first()
    if user:
        return Response(get_user_data(user), status=status.HTTP_200_OK)
    else:
        return Response(["No such user!"], status=status.HTTP_404_NOT_FOUND)