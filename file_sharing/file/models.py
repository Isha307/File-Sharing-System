from django.db import models
from django.contrib.auth.models import UserManager, AbstractBaseUser, PermissionsMixin
from django.utils import timezone
from django.core.exceptions import ValidationError
# Create your models here.

class CustomUserManager(UserManager):
    def _create_user(self, email, password, **extra_field):
        if not email:
            raise ValueError("You have not provided your email")
        
        email = self.normalize_email(email)
        user = self.model(email = email, **extra_field)
        user.set_password(password)
        user.save(using=self._db)

        return user
    
    def create_user(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)
    
    def create_superuser(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self._create_user(email, password, **extra_fields)
    
class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(blank=True, default='', unique=True)
    name = models.CharField(max_length=255, blank=True, default='')

    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    date_joined = models.DateTimeField(default=timezone.now)
    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
    
    def get_full_name(self):
        return self.name
    
    def get_short_name(self):
        return self.name or self.email.split('@')[0]
    
class files(models.Model):
    def valid_file_extension(value):
        valid_extensions = ['.pptx','.doc','.docx','.xlsx']
        if value.file.content_type not in valid_extensions:
            raise ValidationError(u'File not Supported')

    user = models.ForeignKey('User', on_delete = models.CASCADE)
    upload_date = models.DateTimeField(default=timezone.now)
    title = models.CharField(max_length=255, default='')
    upload_file = models.FileField(upload_to='files',validators=[valid_file_extension] ,max_length=250, default=None)

    class Meta:
        verbose_name = 'files'

    def __str__(self):
        return self.name

class Client(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name