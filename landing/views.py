from django.shortcuts import render
from landing.models import *
from landing.serializers import *
from rest_framework.decorators import api_view
from utils.views import respons_setup
from rest_framework.response import Response
# Create your views here.

@api_view(['GET'])
def landingHeroData(request):
   try:
        all_landing = LandingHero.objects.all()
        all_landing_data_serializer = LandingHeroSerializer(all_landing, many=True)
        all_landing_data = all_landing_data_serializer.data
        return respons_setup('get all landing', all_landing_data, 200)
   except Exception as error:
        return respons_setup('there was an servier said error', {}, 400)




@api_view(["GET"])
def aboutData(request):
     try:
          all_about_data = About.objects.all()
          all_about_data_serializer = AboutSerializer(all_about_data,many=True)
          all_about_data = all_about_data_serializer.data
          return respons_setup('get all landing subscription', all_about_data, 200)
     except Exception as error:
        return respons_setup('there was an servier said error', {}, 400)
     
     

@api_view(["GET"])
def teamProfileData(request):
     try:
          all_team_profile_data = TeamProfile.objects.all()
          all_team_profile_data_serializer = TeamProfileSerializer(all_team_profile_data,many=True)
          all_team_profile_data = all_team_profile_data_serializer.data
          return respons_setup('get all landing subscription', all_team_profile_data, 200)
     except Exception as error:
        return respons_setup('there was an servier said error', {}, 400)
     




@api_view(["GET"])
def questionAndAnswerData(request):
     try:
          all_question_answer_data = FrequentlyAskedQuestions.objects.all()
          all_question_answer_data_serializer = FrequentlyAskedQuestionsSerializer(all_question_answer_data,many=True)
          all_question_answer_data = all_question_answer_data_serializer.data
          return respons_setup('get all landing subscription', all_question_answer_data, 200)
     except Exception as error:
        return respons_setup('there was an servier said error', {}, 400)
     



@api_view(["GET"])
def helpAboutData(request):
     try:
          all_help_about_data = HelpAbout.objects.all()
          all_help_about_data_serializer = HelpAboutSerializer(all_help_about_data,many=True)
          all_help_about_data = all_help_about_data_serializer.data
          return respons_setup('get all landing subscription', all_help_about_data, 200)
     except Exception as error:
        return respons_setup('there was an servier said error', {}, 400)
     
     
     
     

@api_view(["POST","GET"])
def helpContactData(request):
     try:
          if request.method == 'GET':
               all_help_contact_data = HelpContact.objects.all()
               all_help_contact_data_serializer = HelpContactSerializer(all_help_contact_data,many=True)
               all_help_contact_data = all_help_contact_data_serializer.data
               return respons_setup('get all landing subscription', all_help_contact_data, 200)
          
          if request.method == 'POST':
               serializer = HelpContactSerializer(data=request.data)
               if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data)
          
     except Exception as error:
        return respons_setup('there was an servier said error', {}, 400)
     
     




@api_view(["GET"])
def landingSubscriptionData(request):
     try:
          all_landing_subscription = LandingSubscription.objects.all()
          all_landing_subscription_data_serializer = LandingSubscriptionSerializer(all_landing_subscription,many=True)
          all_landing_subscription_data = all_landing_subscription_data_serializer.data
          return respons_setup('get all landing subscription', all_landing_subscription_data, 200)
     except Exception as error:
        return respons_setup('there was an servier said error', {}, 400)
     