from django.db import models



class Session(models.Model):
   years = models.CharField(max_length=30, blank=True, null=True)
   def __str__(self):
       return self.years


class Tag(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    name_bn = models.CharField(max_length=50, blank=True, null=True)
    def __str__(self):
       return self.name
