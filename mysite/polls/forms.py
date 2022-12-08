from django import forms
from .models import Comment
"""
    comment - feedback of the user
    email - the email of the user
"""

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'


# class CommentForm(forms.Form):

#     comment = forms.CharField(max_length=300)
#     email = forms.EmailField()