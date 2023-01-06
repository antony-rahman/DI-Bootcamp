from faker import Faker
from datetime import date
from rent.models import Customer
import random 


fake = Faker()
print(fake.first_name())

rental_date = fake.date_between(start_date =date(2022,1,1))
rand_int = random.randint(0-10)
if rand_int > 5 :
    return_date = None
else:
    return_date = fake.date_between(start_date = rental_date)

rand_idx = random.randint(1, 101)
customer = Customer.objects.get(id=rand_idx)
return_date = fake.date_between(start_date =rental_date)
print(return_date)