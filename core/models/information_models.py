from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=255, unique=True, db_index=True)
    population = models.IntegerField(null=True, blank=True)
    flag = models.ImageField(upload_to='country_flags/', null=True, blank=True)

    def __str__(self) -> str:
        return self.name


class Company(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='companies')
    number_of_employees = models.IntegerField(null=True, blank=True)
    net_worth = models.IntegerField(null=True, blank=True)

    def __str__(self) -> str:
        return self.name
