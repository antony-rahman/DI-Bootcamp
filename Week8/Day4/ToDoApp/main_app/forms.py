from unicodedata import name
from django import forms
from .models import Category

class DateInput(forms.DateInput):
    input_type = 'date'

class CategoryForm(forms.Form):

    name = forms.CharField()
    image = forms.URLField()

class TodoForm(forms.Form):

    title = forms.CharField()
    details = forms.CharField(widget=forms.Textarea(attrs={'rows': 2, 'class': 'details'}))
    deadline_date = forms.DateField(widget=forms.DateInput)
    category = forms.ModelChoiceField(queryset=Category.objects.all())
