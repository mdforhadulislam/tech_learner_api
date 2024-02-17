from rest_framework import serializers, validators
from .models import *

class CategoriesSerializers(serializers.ModelSerializer):
   class Meta:
      model = Categories
      fields = "__all__"
   



