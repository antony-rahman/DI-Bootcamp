from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse
from .models import UserProfile, Posts

# Create your views here.
def index(request):
    return HttpResponse(request, 'homepage.html', {})

def profile(request):
    return HTTPResponse('This is a user profile')

def posts(request, author_id) -> HTTPResponse:
    user = UserProfile.objects.get(author_id) #UserProfileObject
    posts = user.posts.all() #QuerySet
    return render(request, posts.html, {'posts':posts})


