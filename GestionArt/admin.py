from django.contrib import admin
from .models import Client, Vehicle, Task
# Register your models here.

#To manage models in Admin section
admin.site.register(Client)

admin.site.register(Vehicle)

admin.site.register(Task)