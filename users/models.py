from django.db import models

from system.models import BaseUserProfile
from users.constants import USER, USER_TYPES


class UserProfile(BaseUserProfile):
    type = models.PositiveSmallIntegerField(choices=USER_TYPES, default=USER)

    class Meta:
        ordering = ['-joined_at']

    def __str__(self) -> str:
        name = self.full_name if self.full_name else self.user.username.title()
        return name

    @property
    def username(self):
        return self.full_name if self.full_name else self.user.username.title()
