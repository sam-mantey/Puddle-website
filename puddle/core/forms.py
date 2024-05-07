from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        "placeholder": "Your username",
        'class': 'py-3 px-3 rounded-xl outline-teal-500 w-full ',
    }))

    password = forms.CharField(widget=forms.PasswordInput(attrs={
        "placeholder": "Your password",
        'class': 'py-3 px-3 rounded-xl outline-teal-500 w-full ',
    }))

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "email", 'password1', 'password2') 

    username = forms.CharField(widget=forms.TextInput(attrs={
        "placeholder": "Your username",
        'class': 'py-3 px-3 rounded-xl outline-teal-500 w-full ',
    }))

    email = forms.CharField(widget=forms.EmailInput(attrs={
        "placeholder": "Your email address",
        'class': 'py-3 px-3 rounded-xl outline-teal-500 w-full ',
    }))

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        "placeholder": "Your password",
        'class': 'py-3 px-3 rounded-xl outline-teal-500 w-full ',
    }))

    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        "placeholder": "Repeat pasword",
        'class': 'py-3 px-3 rounded-xl outline-teal-500 w-full ',
    }))