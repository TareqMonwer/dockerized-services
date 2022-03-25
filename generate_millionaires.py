"""Create Millionaire records using batches."""
import multiprocessing
import os
import random

import django
# must be in top of django.setup()
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()
from core.models.information_models import Company, Country
from faker import Faker
from core.models import Millionaire

fake = Faker()
N_TO_GENERATE = 5000
countries = Country.objects.values_list('id', flat=True)
companies = Company.objects.values_list('id', flat=True)


def create_millionaire(i):
    Millionaire.objects.create(
        name=fake.name(),
        country_id=random.choice(countries),
        city=fake.city(),
        address=fake.address(),
        company_id=random.choice(companies),
        profession=fake.job(),
        phone=fake.phone_number()
    )


if __name__ == '__main__':
    p = multiprocessing.Pool(50)
    p.map(create_millionaire, range(N_TO_GENERATE))
    p.close()
    p.join()
    print('{} records created: '.format(N_TO_GENERATE))
