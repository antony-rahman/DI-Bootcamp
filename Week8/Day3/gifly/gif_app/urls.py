from django.urls import path
from .views import create_category, homepage_view, create_gif

urlpatterns = [
    path("create_category", create_category, name='create_category'),
    path("home_page", homepage_view, name='home_page'),
    path("create_gif", create_gif, name='create_gif')
    ]