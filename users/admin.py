from django.contrib import admin
from django.contrib.auth.models import User
from users.models import UserProfile


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['id', 'full_name', 'lives_in', 'works_at', 
                    'last_seen', 'joined_at', 'updated_at', 'type']


admin.site.register(UserProfile, UserProfileAdmin)
