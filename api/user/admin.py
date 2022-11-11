from django.contrib import admin
from .models import User


class UsersAdmin(admin.ModelAdmin):
    list_display = ['email', 'first_name', 'last_name', 'phone_number', 'is_recruiter', 'is_staff', 'last_login'] # noqa


# Register your models here.
admin.site.register(User, UsersAdmin)
