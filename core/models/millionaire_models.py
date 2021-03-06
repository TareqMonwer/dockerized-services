from email.policy import default
from django.db import models
from django.contrib.postgres.search import SearchVectorField
from django.contrib.postgres.indexes import GinIndex

from core.models.information_models import Company, Country


class Millionaire(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='profile_pics/', default='system_default.png')
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='millionaires')
    city = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='millionaires')
    profession = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    # https://pganalyze.com/blog/full-text-search-django-postgres
    vector_column = SearchVectorField(null=True)

    class Meta:
        db_table = u'millionaire'
        indexes = [
            GinIndex(fields=['vector_column']),
            models.Index(fields=['name', 'profession',]),
        ]


    def __str__(self):
        return self.name


