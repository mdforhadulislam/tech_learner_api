from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Balance)
admin.site.register(BalanceHistory)
admin.site.register(BalanceCreditRequest)
admin.site.register(BalanceWithdrawRequest)
admin.site.register(Subscription)