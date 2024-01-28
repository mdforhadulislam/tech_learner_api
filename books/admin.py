from django.contrib import admin
from books.models import *

# Register your models here.
admin.site.register(Categories)
admin.site.register(Book)
admin.site.register(FreeBookPage)
admin.site.register(FreeBooks)
admin.site.register(Chapter)
admin.site.register(Pages)