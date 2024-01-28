from django.db import models

# Create your models here.



HISTORY_TYPE = (
    ("-debit", "-debit"),
    ("+credit", "+credit")
)

class Balance_History(models.Model):
   history_type = models.CharField(
        max_length=20, choices=HISTORY_TYPE, default=' ', blank=True, null=True)
   amount = models.CharField(max_length=50, blank=True, null=True)
   date = models.DateTimeField(null=True)


class Balance(models.Model):
   main_balance = models.CharField(max_length=50, blank=True, null=True)
   balance_history = models.ManyToManyField(Balance_History)
   