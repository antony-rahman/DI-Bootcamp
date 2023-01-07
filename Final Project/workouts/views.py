from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
from django.http import HttpResponse
from django.template import loader

from .models import Workout
from .forms import WorkoutForm

@login_required
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

@login_required
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

def register(request):
    print('here')
    if request.method == 'POST':  
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()  
            messages.success(request, 'User account created successfully')  
            context = {  
                'form':form  
            }
            return redirect('/accounts/login')
        else:
            context = {  
                'form':form  
            }
            return render(request, 'registration/new.html', context)  

    else:  
        form = UserCreationForm()  
        context = {  
            'form':form  
        }
        return render(request, 'registration/new.html', context)  

def log_out(request):
    logout(request)
    messages.success(request, 'You have been logged out')
    return redirect('/accounts/login/')
