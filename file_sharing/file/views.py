from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .models import User
from django.views import View
from .forms import ClientForm
from django.contrib import messages

def home(request):
    return render(request, 'file/home.html')

def register(request):
    form = UserCreationForm()
    
    if request.method == 'POST':
        if form.is_valid():
            form.save()
    context = {'form':form}
    return render(request, 'file/signup.html', context)


def login(request):

    context = {}
    return render(request, 'file/login.html')

