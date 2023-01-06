from django.shortcuts import render
from .forms import VehicleSizeform, Vehicleform, Rental
import faker
from .models import VehicleSize, VehicleType,Customer, Vehicle

fake = faker.Faker(['pt-PT'])

# Create your views here.
def fill_customer_table():
        for i in range (100):
            customer = Customer(
                first_name= fake.first_name(), 
                last_name= fake.last_name(),
                email = fake.email(),
                phone_number = fake.phone_number(),
                address = fake.address(),
                city = fake.city(),
                country = fake.country(),
                )
            customer.save()

def fill_rentals():
    pass

def rentals_page(request):
    rentals = Rental.objects.all()
    return render(request, 'rentals_page.html', {'rentals':rentals})

def rental_details(request, id):
    rental = Rental.objects.get(id = id)
    return render(request, 'rental_details.html', {'rental':rental})

def customers_view(request):
    customers = Customer.objects.all()
    return render(request, 'rental.html', {'customers':customers})
# def add_customer(request):
#     pass
# def add_rentals(request):
#     pass
def add_vehicles(request):
    context = {'form': VehicleSizeform}
    if request.method == 'POST':
        vehicle_form = VehicleSizeform(request.POST)
        if vehicle_form.is_valid():
            filled_form = vehicle_form.save()            
    return render(request, 'add_vehicle.html', context)    

def rentals(request):
    # click on customer to go to customer page; click on vehicle to go to vehicle page; click a button to return the vehicle.
    rentals = Rental.objects.all()
    return render(request, 'rentals_page.html', {'rentals': rentals})

def vehicles_page(request):
    # click on a vehicle to see its details. Make a visual sign to show which vehicles are currently rented and which are available.
    vehicles = Vehicle.objects.all()
    return render(request, 'vehicles.html', {'vehicles': vehicles})