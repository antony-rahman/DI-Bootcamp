from django.urls import path
from .views import add_vehicles, vehicles_page, rentals, rental_details

urlpatterns = [
    path('add_vehicles', add_vehicles, name = 'add_vehicles'),
    path('vehicles', vehicles_page, name = 'vehicles'),
    path('rentals', rentals, name = 'rentals'),
    path('rental_details/<int:id>', rental_details, name = 'rental_details'),
]
