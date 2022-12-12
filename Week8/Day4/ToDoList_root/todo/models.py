from django.urls import reverse
from django.db import models
from datetime import datetime, date

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length = 20)
    image = models.URLField()

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self):
        return reverse('category', args=[self.id])


class Todo(models.Model):
    title = models.CharField(max_length = 20)
    details = models.CharField(max_length=500)
    has_been_done = models.BooleanField(default=False)
    date_creation = models.DateField(auto_now_add=True)
    date_completion = models.DateField(null=True)
    deadline_date = models.DateField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='category')

    def __str__(self) -> str:
        return f"Task: {self.title}, created: {self.date_creation}, deadline: {self.deadline_date}"
