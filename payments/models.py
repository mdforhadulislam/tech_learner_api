from django.db import models
from django.contrib.auth.models import User


HISTORY_TYPE = (
    ("-Debit", "-Debit"),
    ("+Credit", "+Credit")
)

METHOD_TYPE = (
    ("Bkash", "Bkash"),
    ("Nogod", "Nogod"),
    ("Rokect", "Rokect"),
    ("Upay", "Upay")
)


class BalanceHistory(models.Model):
    history_type = models.CharField(
        max_length=20, choices=HISTORY_TYPE, default=' ', blank=True, null=True)
    amount = models.CharField(max_length=50, blank=True, null=True)
    date = models.DateField(null=True)

    def __str__(self) -> str:
        return f'History Type: {self.history_type} - Amount: {self.amount} - Date: {self.date}'


class Balance(models.Model):
    user_id = models.CharField(max_length=200, blank=True, null=True)
    main_balance = models.CharField(max_length=50, blank=True, null=True)
    balance_history = models.ManyToManyField(BalanceHistory, blank=True)

    def __str__(self) -> str:
        return f'User Id: {self.user_id} Main Balance: {self.main_balance}'


class BalanceCreditRequest(models.Model):
    user_id = models.CharField(max_length=200, blank=True, null=True)
    method = models.CharField(
        max_length=20, choices=METHOD_TYPE, default=' ', blank=True, null=True)
    number = models.CharField(max_length=15, blank=True, null=True)
    trxid = models.CharField(max_length=20, blank=True, null=True)
    credit_amounts = models.CharField(max_length=20, blank=True, null=True)
    is_accepted = models.BooleanField(default=False)

    def __str__(self):
        return f'Method:- {self.method} -  Number:- {self.number} -  Taka:- {self.credit_amounts} - {self.is_accepted}'


class BalanceWithdrawRequest(models.Model):
    user_id = models.CharField(max_length=200, blank=True, null=True)
    withdraw_amount = models.CharField(max_length=20, blank=True, null=True)
    method = models.CharField(
        max_length=20, choices=METHOD_TYPE, default=' ', blank=True, null=True)
    number = models.CharField(max_length=15, blank=True, null=True)
    is_accepted = models.BooleanField(default=False)

    def __str__(self):
        return f'Method:- {self.method} -  Number:- {self.number} -  Taka:- {self.withdraw_amount} - {self.is_accepted}'


class Subscription(models.Model):
    name = models.CharField(max_length=20, blank=True, null=True)
    name_bn = models.CharField(max_length=20, blank=True, null=True)
    price = models.CharField(max_length=20, blank=True, null=True)
    price_bn = models.CharField(max_length=20, blank=True, null=True)
    access_time = models.CharField(max_length=20, blank=True, null=True)
    access_time_bn = models.CharField(max_length=20, blank=True, null=True)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)

    def __str__(self):
        return f'Name: {self.name} - Price: {self.price} - Start Time: {self.start_date} - to - End Time: {self.end_date}'
