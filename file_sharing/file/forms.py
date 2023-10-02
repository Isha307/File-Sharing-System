from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Client

class ClientForm(ModelForm):
    class Meta:
        model = Client
        fields = '__all__'