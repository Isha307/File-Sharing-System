from django.contrib import admin
from .models import files, Client, DownloadToken
# Register your models here


admin.site.register(files)
admin.site.register(Client)
admin.site.register(DownloadToken)