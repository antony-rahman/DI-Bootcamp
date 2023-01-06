from django import forms
from .models import Category
from .validators import check_splcharacter

class CategoryForm(forms.Form):

    name = forms.CharField(min_length=3, max_length=50)

class GifForm(forms.Form):
   
    title = forms.CharField(min_length=3, max_length=50),
    url = forms.URLField(),
    uploader_name = forms.CharField(min_length=3, max_length=50)
    categories = forms.ModelMultipleChoiceField(queryset=Category.objects.all())

    