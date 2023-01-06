from django.urls import reverse
from django.db import models


class Gif(models.Model):
    title = models.CharField(max_length=50)
    url = models.URLField()
    uploader_name = models.CharField(max_length=50)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('show_gif', args = [self.id])


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    gifs = models.ManyToManyField(Gif, related_name='categories')

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('show_category', args = [self.id])


