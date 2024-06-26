from django.db import models
from utils.models import Session, Tag


class Categories(models.Model):
    title = models.CharField(max_length=30, blank=True, null=True)
    titleBn = models.CharField(max_length=30, blank=True, null=True)
    details = models.TextField(blank=True, null=True)
    detailsBn = models.TextField(blank=True, null=True)
    categories_image = models.ImageField(
        upload_to='categories/', blank=True, null=True)
    categories_link = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f'Title: {self.title} - Link: {self.categories_link}'


class FreeBookPage(models.Model):
    book_name = models.CharField(max_length=100, blank=True, null=True)
    book_page_number = models.CharField(max_length=100, blank=True, null=True)
    book_image = models.ImageField(
        upload_to='free_pages/', blank=True, null=True)

    def __str__(self):
        return f"Book Name: {self.book_name} - Book Page Number: {self.book_page_number}"


class FreeBooks(models.Model):
    book_name = models.CharField(max_length=100, blank=True, null=True)
    book_images = models.ManyToManyField(FreeBookPage, blank=True)

    def __str__(self):
        return f"Book Name: {self.book_name}"


class Book(models.Model):
    book_categories = models.ForeignKey(
        Categories, on_delete=models.CASCADE, blank=True, null=True)
    book_title = models.CharField(max_length=50, blank=True, null=True)
    book_title_bn = models.CharField(max_length=50, blank=True, null=True)
    book_details = models.TextField(blank=True, null=True)
    book_details_bn = models.TextField(blank=True, null=True)
    book_tag = models.ManyToManyField(Tag, blank=True)
    book_subject_code = models.CharField(max_length=10, blank=True, null=True)
    book_session = models.ForeignKey(
        Session, on_delete=models.CASCADE, blank=True, null=True)
    book_image = models.ImageField(upload_to='books/', blank=True, null=True)
    free_book_image = models.ForeignKey(
        FreeBooks, on_delete=models.CASCADE, blank=True, null=True)
    book_price = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f"Book Title: {self.book_title} - Book Subject Code: {self.book_subject_code} - Book Price: {self.book_price}"


class Chapter(models.Model):
    book_id = models.ForeignKey(
        Book, on_delete=models.CASCADE, blank=True, null=True)
    book_name = models.CharField(max_length=50, blank=True, null=True)
    chapter_name = models.CharField(max_length=100, blank=True, null=True)
    chapter_number = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return f"Book Name: {self.book_name} - Book Chapter Name: {self.chapter_name} - Book Chapter Number: {self.chapter_number}"


class Pages(models.Model):
    chapter_id = models.ForeignKey(
        Chapter, on_delete=models.CASCADE, blank=True, null=True)
    book_name = models.CharField(max_length=50, blank=True, null=True)
    chapter_name = models.CharField(max_length=100, blank=True, null=True)
    pages_number = models.CharField(max_length=20, blank=True, null=True)
    pages_images = models.ImageField(
        upload_to='book_pages/', blank=True, null=True)

    def __str__(self):
        return f" Book Name: {self.book_name} - Book Chapter Name: {self.chapter_name} - Book Page Number: {self.pages_number}"
