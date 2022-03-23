import django
import os
# must be in top of django.setup()
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from faker import Faker
from core.models import Millionaire

fake = Faker()


for i in range(1000):
    Millionaire.objects.create(
            name=fake.name(),
            country=fake.country(),
            city=fake.city(),
            address=fake.address(),
            company=fake.company(),
            profession=fake.job(),
            phone=fake.phone_number()
    )

