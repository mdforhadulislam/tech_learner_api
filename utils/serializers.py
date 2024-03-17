from rest_framework import serializers, validators
from .models import *



class SessionSerializers(serializers.ModelSerializer):
   class Meta:
      model = Session
      fields = "__all__"
   


class TagSerializers(serializers.ModelSerializer):
   class Meta:
      model = Tag
      fields = "__all__"
   