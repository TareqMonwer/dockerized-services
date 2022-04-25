"""Create Millionaire records using batches."""
import multiprocessing
import random
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


def run():
    p = multiprocessing.Pool(50)
    p.map(create_millionaire, range(N_TO_GENERATE))
    p.close()
    p.join()
    print('{} records created: '.format(N_TO_GENERATE))
