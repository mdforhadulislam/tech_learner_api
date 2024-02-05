from rest_framework import serializers, validators
from .models import *

class LandingHeroSerializer(serializers.ModelSerializer):
    class Meta:
        model = LandingHero
        fields = "__all__"
        



