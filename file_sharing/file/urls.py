"""
URL configuration for file_sharing project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path, include
from .views import home, register, login_page, download_file, FileListView, FileListEncryptedView, UserListView

urlpatterns = [
    path('', home, name ='home' ),
    path('register/', register, name ='register' ),
    path('login/', login_page, name ='login' ),
    path('file-list', FileListView.as_view(), name = 'file-list'),
    path('user-list', UserListView.as_view(), name = 'user-list'),
    path('download/<int:assignment_id>/', download_file, name='download_file'),
    path('file-list-encrypted', FileListEncryptedView.as_view(), name = 'file-list-encrypted'),
    path('verification/', include('verify_email.urls')),	
    # Add other URLs as needed.
]

