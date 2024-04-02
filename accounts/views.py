from rest_framework.decorators import api_view
from rest_framework.response import Response
from utils.views import *
from .serializers import *


@api_view(["GET", "PATCH", "PUT"])
def userProfileInfoGetData(request, user_id):
    try:
        if request.method == 'GET':
            user_profile_info_data = UserProfileInfo.objects.get(
                user_id=user_id)
            user_profile_info_data_serializer = UserProfileInfoSerializers(
                user_profile_info_data)
            user_profile_info_data = user_profile_info_data_serializer.data
            return respons_setup('get single subscription data', user_profile_info_data, 200)

        if request.method == 'PATCH' or request.method == 'PUT':
            user_profile_info_data = UserProfileInfo.objects.get(
                user_id=user_id)
            serializer = UserProfileInfoSerializers(
                user_profile_info_data, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return respons_setup('get all landing subscription', serializer.data, 200)

    except Exception as error:
        return respons_setup('there was an servier said error', {}, 400)


@api_view(["POST"])
def userProfileInfoPostData(request):
    try:
        serializer = UserProfileInfoSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return respons_setup('created user profile', serializer.data, 200)

    except Exception as error:
        print(error)
        return respons_setup('there was an servier said error', {}, 400)


@api_view(["GET", "PATCH", "PUT"])
def accessBookData(request, user_id):
    try:
        if request.method == 'GET':
            all_access_book_data = AccessBook.objects.get(
                user_id=user_id)
            all_access_book_data_serializer = AccessBookSerializers(
                all_access_book_data)
            all_access_book_data = all_access_book_data_serializer.data
            return respons_setup('get all landing subscription', all_access_book_data, 200)

        if request.method == 'PATCH' or request.method == 'PUT':
            all_access_book_data = AccessBook.objects.get(user_id=user_id)
            serializer = AccessBookSerializers(
                all_access_book_data, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return respons_setup('get all landing subscription', serializer.data, 200)

    except Exception as error:
        return respons_setup('there was an servier said error', {}, 400)


@api_view(["GET", "PATCH", "PUT"])
def readedBookData(request, user_id):
    try:
        if request.method == 'GET':
            all_readed_book_data = ReadedBook.objects.get(
                user_id=user_id)
            all_readed_book_data_serializer = ReadedBookSerializers(
                all_readed_book_data)
            all_readed_book_data = all_readed_book_data_serializer.data
            return respons_setup('get all landing subscription', all_readed_book_data, 200)

        if request.method == 'PATCH' or request.method == 'PUT':
            all_readed_book_data = ReadedBook.objects.get(user_id=user_id)
            serializer = ReadedBookSerializers(
                all_readed_book_data, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return respons_setup('get all landing subscription', serializer.data, 200)

    except Exception as error:
        return respons_setup('there was an servier said error', {}, 400)
