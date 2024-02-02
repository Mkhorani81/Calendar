from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import UserInfo
# Register your models here.

UserAdmin.fieldsets[2][1]['fields'] = (
    'is_active',
    'is_staff',
    'is_superuser',
    'groups',
    'user_permissions',
)

UserAdmin.list_display += ('is_student',)
admin.site.register(UserInfo, UserAdmin)
