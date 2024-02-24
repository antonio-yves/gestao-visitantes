from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    fieldsets = (
        (_('personal info'), {'fields': ('username', 'password', 'first_name', 'last_name', 'email', 'avatar',)}),
        (_('permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions',)}),
        (_('important dates'), {'fields': ('last_login', 'date_joined',)}),
    )
    filter_horizontal = ('groups', 'user_permissions',)
