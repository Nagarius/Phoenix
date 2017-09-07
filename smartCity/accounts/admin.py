from django.contrib import admin
from .models import UserInfo, UserType, City

# Register your models here.

admin.site.register(UserInfo)
admin.site.register(UserType)
admin.site.register(City)