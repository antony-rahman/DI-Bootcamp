# Generated by Django 4.1.4 on 2023-01-04 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workouts', '0005_alter_workout_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workout',
            name='duration',
            field=models.IntegerField(default=0, help_text='Enter workout duration (minutes)'),
        ),
    ]
