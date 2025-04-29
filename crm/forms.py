from django import forms
from .models import Customer
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name','email','phone','address']

class RegisterForm(UserCreationForm):
    email=forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ['username','email','password1',]