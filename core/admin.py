from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    # Add custom fields to the "Add User" form
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'first_name', 'last_name', 'city', 'state', 'address', 'phone'),
        }),
    )

    # Add custom fields to the "Change User" form
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name', 'email', 'city', 'state', 'address', 'phone')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

    # display additional fields in the list view (optional)
    list_display = ('username', 'email', 'first_name', 'last_name', 'city', 'state', 'is_staff')

admin.site.register(CustomUser, CustomUserAdmin)