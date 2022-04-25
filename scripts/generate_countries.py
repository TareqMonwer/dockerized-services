"""Create Country records using batches."""
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


def run():
    count = create_countries()
    print("Created {} records.".format(count))
