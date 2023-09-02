from django.db import models
from django.contrib.auth.models import User
from core.models.information_models import Company, Country


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class BaseUserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    full_name = models.CharField(max_length=50, null=True, blank=True)
    image = models.ImageField(upload_to='profile_pics/', default='system_default.png')
    about = models.CharField(max_length=255, null=True, blank=True)
    lives_in = models.ForeignKey(Country, on_delete=models.CASCADE, 
                                related_name='profiles_lives_in', null=True, blank=True)
    works_at = models.ForeignKey(Company, on_delete=models.CASCADE, 
                                related_name='employees_works_at', null=True, blank=True)
    last_seen = models.DateTimeField(auto_now_add=True)
    joined_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
