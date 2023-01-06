from socket import fromshare
from django import forms
from .models import *

class Customerform(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
class Vehicleform(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = '__all__'
class Rentalform(forms.ModelForm):
    class Meta:
        model = Rental
        fields = '__all__'
class Rentalateform(forms.ModelForm):
    class Meta:
        model = RentalRate
        fields = '__all__'
class VehicleSizeform(forms.ModelForm):
    class Meta:
        model = VehicleSize
        fields = '__all__'
class VehicleTypeform(forms.ModelForm):
    class Meta:
        model = VehicleType
        fields = '__all__'
