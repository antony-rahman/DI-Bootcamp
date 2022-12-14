# Generated by Django 4.1 on 2022-08-10 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("gif_app", "0002_alter_category_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="category",
            name="gifs",
            field=models.ManyToManyField(related_name="categories", to="gif_app.gif"),
        ),
        migrations.AlterField(
            model_name="category",
            name="name",
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
