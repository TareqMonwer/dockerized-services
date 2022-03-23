"""Create Millionaire records using batches."""
import multiprocessing
import os

import django
# must be in top of django.setup()
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()
from faker import Faker
from core.models import Millionaire

fake = Faker()
N_TO_GENERATE = 5000


def create_millionaire(i):
    Millionaire.objects.create(
        name=fake.name(),
        country=fake.country(),
        city=fake.city(),
        address=fake.address(),
        company=fake.company(),
        profession=fake.job(),
        phone=fake.phone_number()
    )


if __name__ == '__main__':
    p = multiprocessing.Pool(50)
    p.map(create_millionaire, range(N_TO_GENERATE))
    p.close()
    p.join()
    print('{} record created: '.format(N_TO_GENERATE))
