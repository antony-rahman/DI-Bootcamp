# Generated by Django 4.1.4 on 2023-01-03 14:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workouts', '0002_alter_workout_type'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='workout',
            options={'ordering': ['-date']},
        ),
        migrations.AddField(
            model_name='workout',
            name='date',
            field=models.DateField(default=datetime.datetime(2023, 1, 3, 14, 4, 16, 674621, tzinfo=datetime.timezone.utc)),
        ),
    ]
