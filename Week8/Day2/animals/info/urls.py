from django.urls import path, include
from . import views


urlpatterns = [
    path('family/<int:id>', views.show_family, name='family'), 
    path('animals', views.show_animals, name='animals'),
    path('animal', views.show_animal, name='animal')  
]
