from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from verify_email.email_handler import send_verification_email
from .forms import CreateUserForm
from .models import files,DownloadToken
from django.contrib.auth.models import User
from .serializers import FileSerializer, UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status 
from .renderers import CustomAesRenderer
from django.http import JsonResponse
import random, string

def home(request):
    file_list = files.objects.all()
    return render(request, 'file/home.html',{'file_list': file_list})

def register(request):
    form = CreateUserForm()
    #print(form)
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        #print(form)
        if form.is_valid():
            inactive_user = send_verification_email(request, form)
            inactive_user.cleaned_data['email']
            form.save()
            return redirect('home')
        else:
            messages.info(request, 'Enter the data correctly, Password must contain at least 8 characters.')
            print(form.is_valid())
        
            
    context = {'form':form}
    return render(request, 'file/signup.html', context)

def login_page(request):
    print(request.POST)
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None :
            login(request, user)
            return redirect('home')
        else :
            messages.info(request, 'Username or Password is incorrect')
    context = {}
    return render(request, 'file/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')


def download_file(request, assignment_id):
    # Assume you have a way to determine the user from the request (e.g., through authentication)
    user = request.user
    # Store the token in the database associated with the user and assignment
    download_token= DownloadToken.objects.get()
    token = ''.join(random.choices(string.ascii_letters+string.digits, k=16))
    # Construct the secure download link
    download_link = f"/download-file/{token}"

    response_data = {
        "download-link": download_link,
        "message": "success"
    }

    return JsonResponse(response_data)




class FileListView(APIView):
    def get(self, request):
        file = files.objects.all()
        if file:
            serializer = FileSerializer(file, many=True)
            data = serializer.data
        data = {
            'status': 'success',
            'code' : status.HTTP_200_OK,
            'data': data
            }
        return Response(data, status=status.HTTP_200_OK)

class UserListView(APIView):
    def get(self, request):
        file = User.objects.all()
        if file:
            serializer = UserSerializer(file, many=True)
            data = serializer.data
        data = {
            'status': 'success',
            'code' : status.HTTP_200_OK,
            'data': data
            }
        return Response(data, status=status.HTTP_200_OK)

class FileListEncryptedView(APIView):
    renderer_classes = [CustomAesRenderer]

    def get(self, request):
        file = files.objects.all()
        if file:
            serializer = FileSerializer(file, many=True)
            data = serializer.data
        data = {
            'status': 'success',
            'code' : status.HTTP_200_OK,
            'data': data
            }
        return Response(data, status=status.HTTP_200_OK)