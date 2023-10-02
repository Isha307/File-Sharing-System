from django.contrib import admin
from .models import User, files, Client
# Register your models here

class data(admin.ModelAdmin):
    list_display = ['upload_file']

admin.site.register(User)
admin.site.register(files, data)
admin.site.register(Client)