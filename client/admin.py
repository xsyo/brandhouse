from django.contrib import admin

from .models import Client, ClientProfile


admin.site.register(Client)
admin.site.register(ClientProfile)
