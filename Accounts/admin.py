from django.contrib import admin

from Accounts.models import Admin


@admin.register(Admin)
class Admin(admin.ModelAdmin):
    list_display = ('id', 'username', 'password', 'is_active')
