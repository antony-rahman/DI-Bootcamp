from django.urls import path
from .views import (
    add_director,
    # delete_film,
    update_film,
    update_director,
    director_films,
    search_directors,
    Homepage,
    AddFilm,
    # FilmComments
)
urlpatterns = [
    path('add-film', AddFilm.as_view(), name="add_film"),
    path('homepage', Homepage.as_view(), name="homepage"),
    # path('film_comments', FilmComments.as_view(), name="film_comments"),
    path('add-director', add_director, name='add_director'),
    path('update-film/<int:id>', update_film, name='update_film'),
    path('update-director/<int:id>', update_director, name='update_director'),
    path('director-films/<int:id>', director_films, name='director_films'),
    # path('delete_film/<int:id>', delete_film, name='delete_film'),
    path('search_directors.html', search_directors, name='search_directors')
]
    # path('add-film', add_film, name='add_film'),
