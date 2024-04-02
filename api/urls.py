from django.urls import path, include
from books.views import *

from payments.views import *
from utils.views import *
from .views import *
# from knox import views as knox_views
from accounts.views import *

urlpatterns = [
    # auth/account/ ----user info
    path("auth/account/", userProfileInfoPostData,
         name='create-user-profile-info'),
    path("auth/account/<str:user_id>", userProfileInfoGetData,
         name='get-user-profile-info'),

    # account/access-book
    path("auth/account/access-book/<str:user_id>",
         accessBookData, name='user-access-book'),
    # account/readed-book
    path("auth/account/readed-book/<str:user_id>",
         readedBookData, name='user-readed-book'),


    # auth/balance/ user account balance
    # chart/book-readed/ ----book readed chart
    # chart/site-visted/ ----site visited chart
    # book/ -----all book

    # book/?book-name=book-name|sub-code=304950|session=2023|tag=hello
    # book/<book-id>/ -----single book
    path('book/<str:book_id>/', single_book, name='single-book-data'),
    # book/<book-id>/chapter/ -----all chapter
    # book/<book-id>/chapter/<chapter-id>/ -----chapter datiels
    # book/<book-id>/chapter/<chapter-id>/pages/ -----under chapter all pages
    # book/categories/ ---all categories show
    # book/?categories=hello ---filtering categories.....show under categoris books
    # book/access-book/ --only show user access book
    # book/readed-book/ --only show user access book

    path('utils/session/<str:id>/', session_data, name='utils-session-data'),
    path('utils/tag/<str:id>/', tag_data, name='utils-tag-data'),


    # utils/about/ ---about datiles
    path('utils/about/', aboutData, name='about-data'),
    # utils/about/team-member/ ---about team member datiles
    path('utils/about/team-member/', teamProfileData,
         name='about-team-profile-data'),

    # utils/ques-ans/ ----question and answer section
    path('utils/ques-ans/', questionAndAnswerData,
         name='question-and-answer-data'),
    # utils/help-about/ -----our all deatils
    path('utils/help-about/', helpAboutData, name='help-about-data'),
    # utils/help-contact/ ----contact with us
    path('utils/help-contact/', helpContactData, name='contact-data'),
]
