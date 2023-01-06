from django.db import models


class Person(models.Model):

    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.name + ' ' + self.phone_number

