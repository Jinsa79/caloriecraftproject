class UserCreationForm(forms.ModelForm):

    class Meta:
        model = User 
        fields = ('username')

from django.contrib.auth.forms import UserCreationForm

form .models import CustomUser

class CustomUserCreationForm(UserCreationForm):

    model = CustomUser


    fields = ('username','email','password1','password2')
