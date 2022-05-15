from django.contrib import admin
from django.contrib.auth.models import User
from users.models import UserProfile


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'type']


admin.site.register(UserProfile, UserProfileAdmin)
