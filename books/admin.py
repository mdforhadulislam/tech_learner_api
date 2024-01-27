from django.contrib import admin
from books.models import *

# Register your models here.
admin.site.register(Categories)
admin.site.register(Book)
admin.site.register(Free_book_page)
admin.site.register(Free_books)
admin.site.register(Chapter)
admin.site.register(Pages)