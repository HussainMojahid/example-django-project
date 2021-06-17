import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','ProTwo.settings')
import django
django.setup()
from faker import Faker
from AppTwo.models import users
from random import random
fakegen = Faker()

def populate(N=5):
    for entry in range(N):
        fname= fakegen.first_name()
        lname = fakegen.last_name()
        email = fakegen.email()

    
        users_l = (users.objects.get_or_create(fname = fname, lname = lname, email = email))[0]


print("Data creating")
populate(10)
print("done")