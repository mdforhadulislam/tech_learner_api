from django.urls import path, include
from .views import *
from knox import views as knox_views
from accounts.views import *

urlpatterns = [
    path('auth/login/', login, name='login'),
    path('auth/register/', register, name='register'),
    path('auth/logout/', knox_views.LogoutView.as_view(), name='logout'), 
]