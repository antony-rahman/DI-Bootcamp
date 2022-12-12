from django.urls import path
from .views import create_todo, display, complete


urlpatterns = [
    path("create_todo", create_todo, name='create_todo'),
    path("display", display, name='display'),
    path("done/<int:object_id>", complete, name='complete')
    

]