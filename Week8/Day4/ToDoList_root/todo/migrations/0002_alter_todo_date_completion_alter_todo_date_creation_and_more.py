# Generated by Django 4.1 on 2022-08-10 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='date_completion',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='todo',
            name='date_creation',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='todo',
            name='deadline_date',
            field=models.DateField(),
        ),
    ]
