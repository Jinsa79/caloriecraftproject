from django import forms
from django.contrib.auth.models import User

class UserCreationForm(forms.ModelForm):

    class Meta:
        model = User 
        fields = ('username',)

from django.contrib.auth.forms import UserCreationForm

from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):

    model = CustomUser

    fields = ('username','email','password1','password2')


