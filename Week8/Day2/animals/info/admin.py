from django.contrib import admin

# Register your models here.
from .models import Animal, Family

admin.site.register(Animal)
admin.site.register(Family)

