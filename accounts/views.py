from rest_framework.decorators import api_view
from rest_framework.response import Response
# from rest_framework.authtoken.serializers import AuthTokenSerializer
# from knox.auth import AuthToken, TokenAuthentication
# from rest_framework import status
# from knox.models import AuthToken 
from utils.views import *
from .serializers import *
# import json


# def serialize_user(user):
#     return {
#         "username": user.username,
#         "email": user.email,
#         "first_name": user.first_name,
#         "last_name": user.last_name
#     }

 
# # this is login api only post username and password
# @api_view(['POST'])
# def login(request):
#     serializer = AuthTokenSerializer(data=request.data)
#     request_token = request.headers['Authorization']
#     print(request_token)
#     get_user = TokenAuthentication.validate_user(request_token,request_token)
#     print(get_user)
#     serializer.is_valid(raise_exception=True)
#     user = serializer.validated_data['user']
#     _, token = AuthToken.objects.create(user)
#     return respons_setup('login success', token, 200)


# # when create new user post username password email first_name and last_name
# @api_view(['POST'])
# def register(request):
#     serializer = RegisterSerializer(data=request.data)
#     if serializer.is_valid(raise_exception=True):
#         user = serializer.save()
#         _, token = AuthToken.objects.create(user)
#         user_data = {
#             "user_info": serialize_user(user),
#             "token": token,
#             'status': 200
#         }
#         return respons_setup('register succes', user_data, 200)


@api_view(["GET"])
def userProfileInfoGetData(request,user_id):
    try:
        if request.method == 'GET':
            user_profile_info_data = UserProfileInfo.objects.get(user_id=user_id)
            user_profile_info_data_serializer = UserProfileInfoSerializers(user_profile_info_data)
            user_profile_info_data = user_profile_info_data_serializer.data
            return respons_setup('get single subscription data', user_profile_info_data, 200)
    except Exception as error:
      print(error)
      return respons_setup('there was an servier said error', {}, 400)




@api_view(["POST"])
def userProfileInfoPostData(request,user_id):
    try:
        if request.method == 'POST':
            serializer = UserProfileInfoSerializers(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return respons_setup('created user profile', serializer.data, 200)
        
    except Exception as error:
      print(error)
      return respons_setup('there was an servier said error', {}, 400)
  


