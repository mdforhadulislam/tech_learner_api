from datetime import datetime
from django.db import models
from django.contrib.auth.models import User
from books.models import Book
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
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    user_profile_image = models.ImageField(
        upload_to='profile/', blank=True, null=True)
    mobile_number = models.CharField(max_length=20, blank=True, null=True)
    blood_group = models.CharField(
        max_length=20, choices=BLOOD_GROUP, default=' ', blank=True, null=True)
    institute_name = models.CharField(max_length=200, blank=True, null=True)
    balance = models.ForeignKey(Balance,blank=True, null=True, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.mobile_number
    
    
    
class BookReadedChartData(models.Model):
    name  = models.CharField(max_length=12, blank=True, null=True)
    date = models.DateField( default=datetime.now(), blank=True, null=True)
    book_readed_number = models.CharField(max_length=12, blank=True, null=True)
    def __str__(self):
        return f'{self.name} - {self.date}'
   
   
class SiteVisitedChartData(models.Model):
    name  = models.CharField(max_length=12, blank=True, null=True)
    date = models.DateField( default=datetime.now(), blank=True, null=True)
    site_visited_number = models.CharField(max_length=12, blank=True, null=True)
    def __str__(self):
        return f'{self.name} - {self.date}'




class UserBookReadedChart(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=20, blank=True, null=True)
    datas = models.ManyToManyField(BookReadedChartData, blank=True)
    def __str__(self):
        return  f'{self.name}'
    
class UserSiteVisitedChart(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=20, blank=True, null=True)
    datas = models.ManyToManyField(SiteVisitedChartData, blank=True)
    def __str__(self):
        return  f'{self.name}'




class AccessBook(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    access_book = models.ManyToManyField(Book, blank=True)


class ReadedBook(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    readed_book = models.ManyToManyField(Book, blank=True)