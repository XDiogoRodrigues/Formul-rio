from django.contrib import admin

from .models import UserSystem


@admin.register(UserSystem)
class UserSystemAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'email', 'create', 'modified', 'active')
