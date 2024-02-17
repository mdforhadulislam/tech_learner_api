from rest_framework import serializers, validators
from .models import *

class CategoriesSerializers(serializers.ModelSerializer):
   class Meta:
      model = Categories
      fields = "__all__"
   

class FreeBookPageSerializers(serializers.ModelSerializer):
   class Meta:
      model = FreeBookPage
      fields = "__all__"
      


class BookSerializers(serializers.ModelSerializer):
   class Meta:
      model = Book
      fields = "__all__"



class ChapterSerializers(serializers.ModelSerializer):
   class Meta:
      model = Chapter
      fields = "__all__"



class PagesSerializers(serializers.ModelSerializer):
   class Meta:
      model = Pages
      fields = "__all__"
