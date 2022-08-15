import json
import jwt
from rest_framework.decorators import api_view
from .serializers import UserSerializer
from rest_framework.response import Response
from rest_framework import status
from .models import User
from .services import get_user_data


@api_view(['POST'])
def create_user(request):
    user_serializer = UserSerializer(data=json.loads(request.body))
    if user_serializer.is_valid():
        user_serializer.save()
        return Response("User has been successfully created!", status=status.HTTP_201_CREATED)
    else:
        return Response(user_serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)


@api_view(['GET'])
def get_user(request, id: int):
    user = User.objects.filter(pk=id).first()
    if user:
        return Response(get_user_data(user), status=status.HTTP_200_OK)
    else:
        return Response(["No such user!"], status=status.HTTP_404_NOT_FOUND)