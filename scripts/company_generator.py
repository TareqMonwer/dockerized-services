"""Create Country records using batches."""
import multiprocessing
import random
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


def run():
    N_TO_GENERATE = 5000
    p = multiprocessing.Pool(50)
    p.map(create_companies, range(N_TO_GENERATE))
    p.close()
    p.join()
    print('{} record created: '.format(N_TO_GENERATE))
