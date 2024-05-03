from django import forms
from .models import CustomUser
from django.contrib.auth.forms import AuthenticationForm


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ['username', 'password']
        

class UserLoginForm(AuthenticationForm):
    class Meta:
        model = CustomUser

