from django.db import models
from django.urls import reverse

# Create your models here.

class Gif_model(models.Model):
    title = models.CharField(max_length=100)
    url = models.URLField()
    uploader_name = models.CharField(max_length = 69)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title + ' ' + self.url

    def get_absolute_url(self):
        return reverse('show_gif', args = [self.id])


class Category_model(models.Model):
    name = models.CharField(max_length=100)
    gifs = models.ManyToManyField(Gif_model, related_name='categories', blank=True)

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self):
        return reverse('show_category', args = [self.id])