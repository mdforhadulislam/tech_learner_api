from django.urls import path, include
from books.views import *

from landing.views import *
from payments.views import *
from utils.views import *
from .views import *
# from knox import views as knox_views
from accounts.views import *

urlpatterns = [
#     path('auth/login/', login, name='login'),
#     path('auth/register/', register, name='register'),
#     path('auth/logout/', knox_views.LogoutView.as_view(), name='logout'),
    # auth/account/ ----user info
    # auth/balance/ user account balance
    # chart/book-readed/ ----book readed chart
    # chart/site-visted/ ----site visited chart
    # book/ -----all book
    # book/?book-name=book-name|sub-code=304950|session=2023|tag=hello
    # book/<book-id>/ -----single book
    # book/<book-id>/chapter/ -----all chapter
    # book/<book-id>/chapter/<chapter-id>/ -----chapter datiels 
    # book/<book-id>/chapter/<chapter-id>/pages/ -----under chapter all pages
    # book/categories/ ---all categories show
    # book/?categories=hello ---filtering categories.....show under categoris books
    # book/access-book/ --only show user access book
    # book/readed-book/ --only show user access book
    # subscription/ --show all Subscription
    
    
    
   #  land/hero/ ---show hero all data
    path('land/hero/', landingHeroData, name='landing-hero-data'),
    # land/subscription/ ---show all subscription plan
    path('land/subscription/', landingSubscriptionData, name='landing-subscription-data'),
    path('land/subscription/<str:id>/', subscription_single_data, name='landing-single-subscription-data'),
    
    
    path('land/categories/',all_categories, name='landing-categories-data'),
    path('land/categories/<str:id>/',under_categories_book, name='landing-categories-data'),
    
    # land/about/ ---about datiles 
    # land/about/team-member/ ---about team member datiles 
    # land/ques-ans/ ----question and answer section
    # land/help-about/ -----our all deatils
    # land/help-contact/ ----contact with us
    
    path('utils/session/<str:id>/',session_data, name='utils-session-data'),
    path('utils/tag/<str:id>/',tag_data, name='utils-tag-data'),
]