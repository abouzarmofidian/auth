from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, Profile

# Register your models here.

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2'),
        }),
    )

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['id', 'user' ,'first_name','last_name']