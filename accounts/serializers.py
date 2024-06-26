# from django.contrib.auth.models import User
from rest_framework import serializers, validators
from .models import *


# class RegisterSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ("username", "password", "email", "first_name", "last_name")
#         extra_kwargs = {
#             "password": {"write_only": True},
#             "email": {
#                 "required": True,
#                 "allow_blank": False,
#                 "validators": [
#                     validators.UniqueValidator(
#                         User.objects.all(), f"A user with that Email already exists."
#                     )
#                 ],
#             },
#         }

#     def create(self, validated_data):
#         user = User.objects.create_user(
#             username=validated_data["username"],
#             email=validated_data["email"],
#             password=validated_data["password"],
#             first_name=validated_data["first_name"],
#             last_name=validated_data["last_name"]
#         )
#         return user


class UserProfileInfoSerializers(serializers.ModelSerializer):
   class Meta:
      model = UserProfileInfo
      fields = "__all__"
   
   
class AccessBookSerializers(serializers.ModelSerializer):
   class Meta:
      model = AccessBook
      fields = "__all__"
   
   
class ReadedBookSerializers(serializers.ModelSerializer):
   class Meta:
      model = ReadedBook
      fields = "__all__"
   