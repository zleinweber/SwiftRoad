from django.contrib import admin

# Register your models here.
from .models import User, Activity

admin.site.register((User, Activity))
