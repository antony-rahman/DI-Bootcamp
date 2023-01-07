from django.shortcuts import render, redirect
from django.contrib import messages

# Create your views here.
from django.http import HttpResponse
from django.template import loader

from .models import Workout
from .forms import WorkoutForm

def index(request):
    latest_workout_list = Workout.objects.order_by('-date')
    workout_level = Workout.get_level()
    form = WorkoutForm()
    context = {
        'latest_workout_list': latest_workout_list,
        'workout_level': workout_level,
        'form': form
    }
    
    return render(request, 'workouts/index.html', context)

def log_workout(request):
    if request.method == 'POST':
        form = WorkoutForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Workout logged successfully')
            return redirect('/workouts/')
    else:
        form = WorkoutForm()
    return render(request,
                  'workouts/index.html',
                  {
                      'form': form
                  })

