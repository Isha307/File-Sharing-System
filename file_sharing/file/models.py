from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.exceptions import ValidationError
import random
# Create your models here.


class Client(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class files(models.Model):
    def valid_file_extension(value):
        valid_extensions = ['application/msword','application/vnd.ms-excel','application/vnd.openxmlformats-officedocument.presentationml.presentation']
        print(value.file.content_type)
        if value.file.content_type not in valid_extensions:
            raise ValidationError(u'File not Supported')

    user = models.ForeignKey(User, on_delete = models.CASCADE)
    upload_date = models.DateTimeField(default=timezone.now)
    title = models.CharField(max_length=255, default='')
    upload_file = models.FileField(upload_to='files',validators=[valid_file_extension], default=None)
    
    class Meta:
        verbose_name = 'files'

    def __str__(self):
        return self.title

class DownloadToken(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    file = models.ForeignKey(files, on_delete=models.CASCADE, default='')
    assignment_id = models.CharField(max_length=1000000, default=random.randint(1,1000000))
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.assignment_id

