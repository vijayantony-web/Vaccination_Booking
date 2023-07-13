from enum import unique
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserRegisterForm(UserCreationForm):
    email=forms.EmailField(required=True)

    class Meta:#nested name space will be given
        model=User 
        fields = ['username','email','password1','password2']

choices=["Book1","Book2","Book3"]
class UserUpdateForm(forms.Form):
    book_name = forms.ChoiceField(choices=[])
    def __init__(self, book_choices, *args, **kwargs):
        super(UserUpdateForm, self).__init__(*args, **kwargs)
        self.fields['book_name'].choices = book_choices