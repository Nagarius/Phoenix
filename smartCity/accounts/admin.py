from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import UserInfo, UserType, City

# Register your models here.


# Adds the extended user table to the admin page

# NOTE: Need to add functionality to get pk from userinfo and give it to usertype as per
#      functionality of registration page
class UserInfoInline(admin.StackedInline):
    model = UserInfo

class UserAdmin(UserAdmin):
    inlines = (UserInfoInline, )


# Adds userType and City tables to admin page.
admin.site.register(UserType)
admin.site.register(City)

# Deloads the default user table and reloads the custom one.
admin.site.unregister(User)
admin.site.register(User, UserAdmin)