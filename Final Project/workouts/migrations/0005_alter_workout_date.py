# Generated by Django 4.1.4 on 2023-01-03 14:05

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('workouts', '0004_alter_workout_date_alter_workout_duration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workout',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
