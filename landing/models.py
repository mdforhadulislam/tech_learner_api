from django.db import models
from payments.models import *

# Create your models here.
class LandingHero(models.Model):
   title1 = models.CharField(max_length=20, blank=True, null=True)
   title2 = models.CharField(max_length=20, blank=True, null=True)
   title3 = models.CharField(max_length=20, blank=True, null=True)
   description = models.TextField(blank=True, null=True)
   book_image_1 =  models.ImageField(upload_to='landing/hero/', blank=True, null=True)
   book_image_2 =  models.ImageField(upload_to='landing/hero/', blank=True, null=True)
   book_image_3=  models.ImageField(upload_to='landing/hero/', blank=True, null=True)
   book_image_4=  models.ImageField(upload_to='landing/hero/', blank=True, null=True)
   book_banar1=  models.ImageField(upload_to='landing/hero/', blank=True, null=True)
   book_banar2=  models.ImageField(upload_to='landing/hero/', blank=True, null=True)
   


class LandingSubscription(models.Model):
   title1 = models.CharField(max_length=20, blank=True, null=True)
   description = models.TextField(blank=True, null=True)
   offer_box = models.ManyToManyField(Subscription,blank=True)
   
   
   

class TeamProfile(models.Model):
   name =  models.CharField(max_length=50, blank=True, null=True)
   title =  models.CharField(max_length=50, blank=True, null=True)
   image = models.ImageField(upload_to='landing/about/', blank=True, null=True)



class About(models.Model):
   title = models.CharField(max_length=50, blank=True, null=True)
   description = models.TextField(blank=True, null=True)
   title1 = models.CharField(max_length=100, blank=True, null=True)
   description1 = models.TextField(blank=True, null=True)
   image_banar =  models.ImageField(upload_to='landing/about/', blank=True, null=True)
   title2 = models.CharField(max_length=100, blank=True, null=True)
   description2 = models.TextField(blank=True, null=True)
   team_section = models.ManyToManyField(TeamProfile, blank=True)
   


class QuestionBox(models.Model):
   question = models.CharField(max_length=150, blank=True, null=True)
   answer = models.TextField(blank=True, null=True)


class FrequentlyAskedQuestions(models.Model):
   title = models.CharField(max_length=50, blank=True, null=True)
   description = models.TextField(blank=True, null=True)
   question_box = models.ManyToManyField(QuestionBox, blank=True)