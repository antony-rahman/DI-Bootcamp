from django import forms
from .validators import check_splcharacter


class SearchForm(forms.Form):
    name = forms.CharField(max_length=50, validators=[check_splcharacter], required= False),
    phone = forms.CharField(max_length=50, validators=[check_splcharacter], required= False)