from django.db import models
from utils.models import Session



class Categories(models.Model):
   title = models.CharField(max_length=30, blank=True, null=True)
   titleBn = models.CharField(max_length=30, blank=True, null=True)
   details = models.TextField(blank=True, null=True)
   detailsBn = models.TextField(blank=True, null=True)
   categories_image = models.ImageField(upload_to='categories/', blank=True, null=True)
   categories_link = models.CharField(max_length=100, blank=True, null=True)
   
   def __str__(self):
        return self.title



class Book(models.Model):
   book_title = models.CharField(max_length=30, blank=True, null=True)
   book_title_bn = models.CharField(max_length=30, blank=True, null=True)
   book_details = models.TextField(blank=True, null=True)
   book_details_bn = models.TextField(blank=True, null=True)
   book_subject_code = models.CharField(max_length=10, blank=True, null=True)
   book_session =  models.ForeignKey(Session, on_delete=models.CASCADE)
   book_image =  models.ImageField(upload_to='books/', blank=True, null=True)
      
   def __str__(self):
        return self.book_title

   