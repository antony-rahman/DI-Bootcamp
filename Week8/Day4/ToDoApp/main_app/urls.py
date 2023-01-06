from django.urls import path
from .views import (
    create_category, 
    create_todo, 
    category, 
    todo_done,
    home)

urlpatterns = [
    path("add_category", create_category, name = 'create_category'),
    path("add_todo", create_todo, name = 'create_todo'),
    path("category/<int:id>", category, name="category"),
    path("todo_done/<int:id>", todo_done, name="todo_done"),
    path("", home, name="homepage")
]
