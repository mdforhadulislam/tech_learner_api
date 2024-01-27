from django.db import models

# Create your models here.
class Session(models.Model):
   years = models.CharField(max_length=30, blank=True, null=True)
   
   def __str__(self):
       return self.years
   