from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Users


class UsersAdmin(UserAdmin):
    model = Users
    list_display = (
        'username', 'name', 'surname', 'last_name', 'phone', 'auto_working_time', 'is_active', 'created_at',
        'updated_at')

    search_fields = ('username', 'name', 'surname', 'phone')
    ordering = ('username',)


admin.site.register(Users, UsersAdmin)
