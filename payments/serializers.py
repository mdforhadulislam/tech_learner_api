from rest_framework import serializers, validators

from .models import *



class SubscriptionSerializers(serializers.ModelSerializer):
   class Meta:
      model = Subscription
      fields = "__all__"