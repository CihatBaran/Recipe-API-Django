from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from core.models import CustomUser


@admin.register(CustomUser)
class AdminUser(UserAdmin):
    ordering = ['id']
    list_display = ['email', 'name']
    list_filter = ["id"]
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal Info', {'fields': ('name',)}),
        (
            'Permissions', {
                'fields': ('is_active', 'is_staff', 'is_superuser')}
        ),
        ('Important Dates', {'fields': ('last_login',)}),

    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )

    class Meta:
        model = CustomUser
