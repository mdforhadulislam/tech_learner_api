from django.shortcuts import render
from landing.models import *
from landing.serializers import *
from rest_framework.decorators import api_view
from payments.serializers import SubscriptionSerializers
from utils.views import respons_setup

# Create your views here.

@api_view(['GET'])
def subscription_single_data(request,id):
   try:
        subscription_data = Subscription.objects.get(id=id)
        single_subscription_data_serializer = SubscriptionSerializers(subscription_data)
        single_subscription_data = single_subscription_data_serializer.data
        return respons_setup('get single subscription data', single_subscription_data, 200)
   except Exception as error:
      print(error)
      return respons_setup('there was an servier said error', {}, 400)
