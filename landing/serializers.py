from rest_framework import serializers, validators
from .models import *

class LandingHeroSerializer(serializers.ModelSerializer):
    class Meta:
        model = LandingHero
        fields = "__all__"
        

class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = "__all__"
        
        

class TeamProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamProfile
        fields = "__all__"
        
        
        
class FrequentlyAskedQuestionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = FrequentlyAskedQuestions
        fields = "__all__"
        
        
        
        
class HelpAboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = HelpAbout
        fields = "__all__"
        
        
        

        
class HelpContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = HelpContact
        fields = "__all__"
        
        
        

class LandingSubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = LandingSubscription
        fields = "__all__"