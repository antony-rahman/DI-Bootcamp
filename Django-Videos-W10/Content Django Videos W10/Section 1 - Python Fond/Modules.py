# Module is basically a file containing a set of functions to include in your app. Also known as package.

# Core

from validators import validate_email
from camelcase import CamelCase
import datetime
from datetime import date

import time

today = datetime.date.today()
today = date.today()
print(today)
timestamp = time.time()
# time.sleep(10.0)
print(today)

# pip modules - pip3 install camelcase
# import camelcase
camel = CamelCase()
text = 'hello there peeps'
print(camel.hump(text))


# import from other files
email = 'daniel#devIns.com'

if validate_email(email):
    print('the email is Valid')
else:
    print('email not valid')
