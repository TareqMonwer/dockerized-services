from django.conf import settings
from django.db import models

from system.models import BaseUserProfile
from users.constants import USER, USER_TYPES


class UserProfile(BaseUserProfile):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, 
                                on_delete=models.CASCADE, related_name='user_profile')
    type = models.PositiveSmallIntegerField(choices=USER_TYPES, default=USER)

    class Meta:
        ordering = ['-joined_at']

    def __str__(self) -> str:
        name = self.full_name if self.full_name else self.user.username.title()
        return name


