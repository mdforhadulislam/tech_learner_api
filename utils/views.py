 
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .models import *
from .serializers import *


def respons_setup(message: str, data: any, statuss: int):
    return Response({
        'messsage': message,
        'data': data,
        'status': statuss
    }, status.HTTP_200_OK)



@api_view(["GET"])
def session_data(request,id):
   try:
      all_session = Session.objects.get(id=id)
      all_session_data_serializer = SessionSerializers(all_session)
      all_session_data = all_session_data_serializer.data
      return respons_setup('get all categories', all_session_data, 200)
   except Exception as error:
      print(error)
      return respons_setup('there was an servier said error', {}, 400)



@api_view(["GET"])
def tag_data(request,id):
   try:
      all_tag = Tag.objects.get(id=id)
      all_tag_data_serializer = TagSerializers(all_tag)
      all_tag_data = all_tag_data_serializer.data
      return respons_setup('get all categories', all_tag_data, 200)
   except Exception as error:
      print(error)
      return respons_setup('there was an servier said error', {}, 400)

