from django.db import models

# Create your models here.

from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

class Workout(models.Model):
    """The base Workout model class."""

    class WorkoutChoices(models.TextChoices):
        JOGGING = 'JOGGING',_('Jogging')
        SWIMMING = 'SWIMMING',_('Swimming')
        BIKING = 'BIKING',_('Biking')
        YOGA = 'YOGA',_('Yoga')
        PUSHUPS = 'PUSHUPS',_('Pushups')
        SITUPS = 'SITUPS',_('Situps')

    # Fields
    type = models.CharField(
        max_length=20, help_text='Enter workout type', choices=WorkoutChoices.choices
    )

    duration = models.IntegerField(
        default=0, help_text='Enter workout duration (minutes)'
    )

    date = models.DateField(
        default=timezone.now
    )

    # Metadata
    class Meta:
        ordering = ['-date']

    # Methods
    def get_absolute_url(self):
        """Returns the URL to access a particular instance of MyModelName."""
        return reverse('model-detail-view', args=[str(self.id)])

    def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)."""
        return "Workout %d of type %s" %(self.id, self.type)