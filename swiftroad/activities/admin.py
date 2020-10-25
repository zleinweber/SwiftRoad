from django.contrib import admin

# Register your models here.
from .models import Activity, ActivityType

admin.site.register((Activity, ActivityType))
