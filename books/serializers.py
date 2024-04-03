from rest_framework import serializers, validators
from .models import *


class CategoriesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = "__all__"


class FreeBookPageSerializers(serializers.ModelSerializer):
    class Meta:
        model = FreeBookPage
        fields = ["book_name", "book_page_number", "book_image", "id"]


class FreeBooksSerializers(serializers.ModelSerializer):
    book_images = FreeBookPageSerializers(many=True)

    class Meta:
        model = FreeBooks
        fields = ["book_name", "book_images"]


class BookSerializers(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"


class ChapterSerializers(serializers.ModelSerializer):
    class Meta:
        model = Chapter
        fields = "__all__"


class PagesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Pages
        fields = "__all__"
