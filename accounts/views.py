from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.auth import AuthToken, TokenAuthentication
from rest_framework import status
from knox.models import AuthToken 
from utils.views import *
from .serializers import *


def serialize_user(user):
    return {
        "username": user.username,
        "email": user.email,
        "first_name": user.first_name,
        "last_name": user.last_name
    }

 
# this is login api only post username and password
@api_view(['POST'])
def login(request):
    serializer = AuthTokenSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = serializer.validated_data['user']
    _, token = AuthToken.objects.create(user)
    return respons_setup('login success', token, 200)


# when create new user post username password email first_name and last_name
@api_view(['POST'])
def register(request):
    serializer = RegisterSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        user = serializer.save()
        _, token = AuthToken.objects.create(user)
        user_data = {
            "user_info": serialize_user(user),
            "token": token,
            'status': 200
        }
        return respons_setup('register succes', user_data, 200)
