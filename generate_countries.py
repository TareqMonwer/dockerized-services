"""Create Country records using batches."""
import os

import django
# must be in top of django.setup()
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()
from core.models.information_models import Country
from faker import Faker

faker = Faker()


def create_countries():
    country_list = list()
    for _ in range(100):
        country_list.append(faker.country())
    
    for country in set(country_list):
        Country.objects.create(
            name=country, 
            population=faker.pyint(10000, 100000000, 1000)
        )
    return len(set(country_list))


if __name__ == "__main__":
    count = create_countries()
    print("Created {} records.".format(count))
