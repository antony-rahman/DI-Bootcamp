from django.contrib import admin
from .models import Gif_model, Category_model


# Register your models here.
admin.site.register(Gif_model)
admin.site.register(Category_model)