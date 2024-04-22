from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile



class RegisterForm(UserCreationForm):
    username = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    first_name = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'placeholder': 'Name'}))
    email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    # password = forms.CharField(max_length=50, required=True, widget=forms.PasswordInput(attrs={'placeholder': 'Passsssword'}))

    class Meta:
        model = User
        fields = ['username', 'first_name', 'email', 'password1', 'password2']


class UpdateProfileForm(forms.ModelForm):

    contact = forms.CharField(widget=forms.Textarea(attrs={'rows': 2}))
    exp = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))

    class Meta:
        model = Profile
        fields = ['contact', 'exp']


class UserRegisterForm(forms.Form):
    username = forms.CharField(max_length=65, widget=forms.TextInput(attrs={"class": "login", "placeholder": "Логин"}), label='')
    password = forms.CharField(max_length=65, widget=forms.PasswordInput(attrs={"class": "password", "placeholder": "Пароль"}), label='')
