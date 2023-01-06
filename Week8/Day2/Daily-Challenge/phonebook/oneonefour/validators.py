import re
from django import forms
from django.core.exceptions import ValidationError
  
def check_splcharacter(str_check): 
 
    string_check= re.compile('[@_!#$%^&*()<>?/\|}{~:]') 

    if(string_check.search(str_check) == None): 
        return str_check
    else: 
        raise forms.ValidationError(f'The name {str_check} is invalid')