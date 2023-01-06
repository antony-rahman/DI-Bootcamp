from django.urls import path
from .views import show_family

urlpatterns = [
    path('family/<int:id>', show_family, name = 'show_family'),
    path('family/<int:id>', show_animal, name = 'show_animal'),
    path('family/<int:id>', show_animals, name = 'show_animals')
]