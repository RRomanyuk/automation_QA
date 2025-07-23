import random
from faker import Faker
from data.data import Person

faker = Faker()
Faker.seed()

def generated_person():
    yield Person(
        full_name=faker.first_name() + ' ' + faker.last_name(),
        first_name=faker.first_name(),
        last_name=faker.last_name(),
        age=random.randint(20, 60),
        salary=random.randint(2000, 15000),
        department=faker.city(),
        email=faker.email(),
        current_address=faker.address(),
        permanent_address=faker.address(),
    )

def generated_file():
    path = rf'C:\dotret\filetest{random.randint(1,1000)}.txt'
    file = open(path, 'w+')
    file.write(f"New text file")
    return file.name, path