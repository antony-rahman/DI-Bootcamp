from tkinter import CASCADE
from django.db import models
from django.urls import reverse



class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    def __str__(self):
        return self.first_name 

class VehicleType(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.vehicle
    def get_absolute_url(self):
        return reverse('vehicle', args = [self.id])
class VehicleSize (models.Model):
    name = models.CharField(max_length=50)

class Vehicle(models.Model):
    vehicle_type = models.ForeignKey(VehicleType, on_delete=models.CASCADE)
    date_created = models.DateField(auto_now=True)
    real_cost = models.FloatField()
    size= models.ForeignKey(VehicleSize,max_length=50, on_delete=models.CASCADE)

class RentalRate(models.Model):
    daily_rate = models.FloatField()
    vehicle_type = models.ForeignKey(VehicleType, related_name='vehicle_type', on_delete=models.CASCADE)
    vehicle_size = models.ForeignKey(VehicleSize, related_name='vehicle_size', on_delete=models.CASCADE)

class Rental (models.Model):
    rental_date = models.DateField(auto_now=True)
    return_date = models.DateField(null = True)
    customer = models.ForeignKey(Customer, related_name='customer', on_delete=models.CASCADE)
    vehicle = models.ForeignKey(Vehicle, related_name='vehicle', on_delete=models.CASCADE)
