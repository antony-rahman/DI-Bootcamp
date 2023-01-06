from tkinter import CASCADE
from django.db import models

# Create your models here.
class UserProfile(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    address = models.CharField(max_length=100, null = True)

    def __srt__(self):
        return self.first_name + ' ' + self.last_name

class Posts(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    author = models.ForeignKey(UserProfile, null=True,  on_delete = models.SET_NULL, related_name = 'posts')
    def __srt__(self):