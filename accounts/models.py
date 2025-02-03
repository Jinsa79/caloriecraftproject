from django.db import models

from django.contrib.auth.forms import UserCreationForm

from .models import CustomUser

# Create your models here.

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password1','password2')