from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# -- USER/PROFILE --
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


# -- LOGIN -- 
class LoginForm(forms.Form):
    username = forms.CharField(max_length=150, label='Username')
    password = forms.CharField(widget=forms.PasswordInput, label='Password')