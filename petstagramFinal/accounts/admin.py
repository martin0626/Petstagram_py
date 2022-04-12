from django.contrib import admin

from petstagramFinal.accounts.models import UserProfile


@admin.register(UserProfile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user']
