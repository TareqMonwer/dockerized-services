"""Create Country records using batches."""
import multiprocessing
import os
import random

import django
# must be in top of django.setup()
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()
from core.models.information_models import Company, Country
from faker import Faker

faker = Faker()
countries = Country.objects.values_list('id', flat=True)


def create_companies(_):
    Company.objects.create(
        name=faker.company(), 
        country_id=random.choice(countries),
        number_of_employees=faker.pyint(10, 1000, 5),
        net_worth=faker.pyint(1000, 100000, 5)
    )


if __name__ == "__main__":
    N_TO_GENERATE = 5000
    p = multiprocessing.Pool(50)
    p.map(create_companies, range(N_TO_GENERATE))
    p.close()
    p.join()
    print('{} record created: '.format(N_TO_GENERATE))
