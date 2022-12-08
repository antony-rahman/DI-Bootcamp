# Generate random String of length 5
# Note: String must be the combination of the UPPER case and lower case letters only. No numbers and a special symbol.
# Hint: use the string module
import string 
import random 
from datetime import date
def random_str(lenght:int):
    random_str = ""
    random_str = ''.join(random.choice(string.ascii_letters)for i in range (5))
    print(random_str)
random_str(5)

today = date.today()
print("Today's date:", today)