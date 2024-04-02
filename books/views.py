from django.shortcuts import render
from rest_framework.decorators import api_view
from books.models import *
from books.serializers import *
from utils.views import respons_setup


@api_view(["GET"])
def all_categories(request):
    try:
        all_categories = Categories.objects.all()
        all_categories_data_serializer = CategoriesSerializers(
            all_categories, many=True)
        all_categories_data = all_categories_data_serializer.data
        return respons_setup('get all categories', all_categories_data, 200)
    except Exception as error:
        print(error)
        return respons_setup('there was an servier said error', {}, 400)


@api_view(["GET"])
def under_categories_book(request, id):
    try:
        single_categories = Categories.objects.get(id=id)
        single_categories_data_serializer = CategoriesSerializers(
            single_categories)
        single_categories_data = single_categories_data_serializer.data

        all_book = Book.objects.filter(
            book_categories=single_categories_data["id"])
        all_book_data_serializer = BookSerializers(all_book, many=True)
        all_book_data = all_book_data_serializer.data

        return respons_setup('get all categories', all_book_data, 200)
    except Exception as error:
        print(error)
        return respons_setup('there was an servier said error', {}, 400)


@api_view(["GET"])
def single_book(request, book_id):
    try:
        single_book_data = Book.objects.get(id=book_id)
        single_book_data_serializer = BookSerializers(single_book_data)
        single_book_data = single_book_data_serializer.data

        return respons_setup('get all categories', single_book_data, 200)
    except Exception as error:
        return respons_setup('there was an servier said error', {}, 400)
