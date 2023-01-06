from operator import index
from django.urls import path
from .views import index, profile

urlpatterns = [
    path('index', index, name='index'),
    path('user_profile', profile, name='profile'),
    path('posts/<int:author_id', profile, name='profile')
    ]