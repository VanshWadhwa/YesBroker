from user.models import Profile
from django.contrib.auth.forms import UserCreationForm
from django.db import models
from django.forms import fields
from django.forms.widgets import EmailInput
from django.contrib.auth.models import User
from django import forms


class UserRegisterForm(UserCreationForm):

    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username' , 'email' , 'password1' , 'password2']

class UserUpdateForm(forms.ModelForm):

    email = forms.EmailField()

    class  Meta:
        model = User
        fields = ['username' , 'email']

class ProfileUpdateForm(forms.ModelForm):

    # image = forms.ImageField()

    class Meta :
        model = Profile
        fields = ['image']
