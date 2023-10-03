from rest_framework import serializers
from .models import files
from django.contrib.auth.models import User


class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = files
        fields = ('user', 'title', 'upload_file')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email')