from django.db import models

# Create your models here.
class Family(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name


class Animal(models.Model):
    name = models.CharField(max_length=50, null=True) 
    legs = models.IntegerField()
    weight = models.FloatField()
    height = models.FloatField()
    speed = models.FloatField()
    family = models.ForeignKey(Family, null = True, on_delete = models.SET_NULL, related_name='posts')

    def __str__(self) -> str:
        return self.name 