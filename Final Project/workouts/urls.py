from django.urls import path
from . import views

app_name = 'workouts'

urlpatterns = [
        path('', views.index, name='index'), 
        path('log_workout/', views.log_workout, name='log_workout'),
]
