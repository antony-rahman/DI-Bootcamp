from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader

from .models import Workout

def index(request):
    latest_workout_list = Workout.objects.order_by('-date')
    template = loader.get_template('workouts/index.html')
    context = {
        'latest_workout_list': latest_workout_list,
    }
    return HttpResponse(template.render(context, request))