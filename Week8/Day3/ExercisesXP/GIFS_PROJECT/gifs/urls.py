from django.urls import path
from .views import create_category, add_gif, homepage, category_view


urlpatterns = [
    path("create_category", create_category, name='create_category'),
    path("add_gif", add_gif, name='add_gif'),
    path("homepage", homepage, name="homepage"),
    path("category/<int:id>", category_view, name="show_category"),
]