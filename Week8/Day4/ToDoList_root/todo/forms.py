from django import forms
from .models import Todo, Category

class DateInput(forms.DateInput):
    input_type = 'date'

class TodoForm(forms.Form):
    title = forms.CharField(max_length=20)
    details = forms.CharField(max_length=400)
    deadline_date = forms.DateField(widget=DateInput)
    category = forms.ModelChoiceField(queryset=Category.objects.all().order_by('name'))


class CategoryForm(forms.Form):
    name = forms.CharField()
    image = forms.URLField()
    