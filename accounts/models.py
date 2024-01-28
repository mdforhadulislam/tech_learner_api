from django.db import models
from django.contrib.auth.models import User
from payments.models import Balance


BLOOD_GROUP = (
    ("A+", "A+"),
    ("B+", "B+"),
    ("O+", "O+"),
    ("AB+", "AB+"),
    ("A-", "A-"),
    ("B-", "B-"),
    ("O-", "O-"),
    ("AB-", "AB-"),
)





class UserProfileInfo(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    user_profile_image = models.ImageField(
        upload_to='profile/', blank=True, null=True)
    mobile_number = models.CharField(max_length=12, blank=True, null=True)
    blood_group = models.CharField(
        max_length=20, choices=BLOOD_GROUP, default=' ', blank=True, null=True)
    institute_name = models.CharField(max_length=200, blank=True, null=True)
    balance = models.ForeignKey(Balance,blank=True, null=True, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.mobile_number