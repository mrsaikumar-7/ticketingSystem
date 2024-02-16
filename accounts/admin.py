from django.contrib import admin
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin
# Register your models here.

class CustomUserAdmin(UserAdmin):
    fieldsets = (
        *UserAdmin.fieldsets,
        (
            'Custom Field Heading',
            {
                "fields": (
                    'is_customer',
                    'is_staff',
                ),
            }
        ),
    )
admin.site.register(CustomUser)