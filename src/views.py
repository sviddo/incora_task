import json
from rest_framework.decorators import api_view
from .serializers import UserSerializer
from rest_framework.response import Response
from rest_framework import status


@api_view(['POST'])
def create_user(request):
    user_serializer = UserSerializer(data=json.loads(request.body))
    if user_serializer.is_valid():
        user_serializer.save()
        return Response("User has been successfully created!", status=status.HTTP_201_CREATED)
    else:
        return Response(user_serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)