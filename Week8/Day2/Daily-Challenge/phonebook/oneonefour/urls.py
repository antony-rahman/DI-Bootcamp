from django.urls import path
from .views import (get_by_name, get_by_number, get_all, search_contact)

urlpatterns = [
    path("name/<str:name>",get_by_name,name='get_by_name'),
    path("number/<str:number>",get_by_number,name='get_by_number'),
    path("", get_all, name="all"),
    path("search",search_contact,name='search_page')
]

