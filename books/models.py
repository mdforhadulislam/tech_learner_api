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


class Free_book_page(models.Model):
   book_name = models.CharField(max_length=100, blank=True, null=True)
   book_page_number = models.CharField(max_length=100, blank=True, null=True)
   book_image = models.ImageField(upload_to='free_pages/', blank=True, null=True)
   
   def __str__(self):
       return f"{self.book_name} - {self.book_page_number}"



class Free_books(models.Model):
   book_name = models.CharField(max_length=100, blank=True, null=True)
   book_images = models.ManyToManyField(Free_book_page)
   def __str__(self):
       return f"{self.book_name}"

   


class Book(models.Model):
   book_title = models.CharField(max_length=50, blank=True, null=True)
   book_title_bn = models.CharField(max_length=50, blank=True, null=True)
   book_details = models.TextField(blank=True, null=True)
   book_details_bn = models.TextField(blank=True, null=True)
   book_subject_code = models.CharField(max_length=10, blank=True, null=True)
   book_session =  models.ForeignKey(Session, on_delete=models.CASCADE)
   book_image =  models.ImageField(upload_to='books/', blank=True, null=True)
   free_book_image = models.ForeignKey(Free_books, on_delete=models.CASCADE)
      
   def __str__(self):
        return f"{self.book_title} - {self.book_subject_code}"


class Chapter(models.Model):
   book_id = models.ForeignKey(Book, on_delete=models.CASCADE)
   book_name = models.CharField(max_length=50, blank=True, null=True)
   chapter_name = models.CharField(max_length=100, blank=True, null=True)
   chapter_number = models.CharField(max_length=20, blank=True, null=True)

   def __str__(self):
        return f"{self.book_name} - {self.chapter_name} - {self.chapter_number}"


class Pages(models.Model):
   chapter_id = models.ForeignKey(Chapter, on_delete=models.CASCADE)
   book_name= models.CharField(max_length=50, blank=True, null=True)
   chapter_name = models.CharField(max_length=100, blank=True, null=True)
   pages_number = models.CharField(max_length=20, blank=True, null=True)
   pages_images = models.ImageField(upload_to='book_pages/', blank=True, null=True)
   
   def __str__(self):
        return f"{self.book_name} - {self.chapter_name} - {self.pages_number}"


