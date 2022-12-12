from django import forms
from .models import Category_model, Gif_model

# GifForm with the fields
# uploader_name
# title
# url : You can use the gifs’ url from the giphy website. Click on the gif you want, and copy the gif link.
# categories : look up ModelMultipleChoiceField

class GifForm (forms.Form):
    uploader_name = forms.CharField()
    title = forms.CharField()
    url = forms.URLField()
    categories = forms.ModelMultipleChoiceField( queryset=Category_model.objects.all().order_by('id'))


class CategoryForm(forms.Form):
    name = forms.CharField(min_length=3, max_length=50)
    