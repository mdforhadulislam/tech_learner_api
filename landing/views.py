from django.shortcuts import render
from landing.models import *
from landing.serializers import *
from rest_framework.decorators import api_view
from utils.views import respons_setup

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