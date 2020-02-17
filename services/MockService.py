from faker import Faker
from models.Customer import Customer
from models.Producers import Producers

fake = Faker('nl_NL')


def Generate(dataType, amount):
    mockData = []
    for _ in range(amount):
        if dataType == 'P':
            mockData.append(__MockProducers())
        elif dataType == 'C':
            mockData.append(__MockCustomers())
    return mockData


def __MockCustomers():
    c = Customer()
    c.id = fake.random_int(min=0, max=99999999, step=1)
    c.name = fake.name()
    c.adress = fake.address()
    return c


def __MockProducers():
    p = Producers()
    p.id = fake.random_int(min=0, max=99999999, step=1)
    p.name = fake.company()
    p.adress = fake.address()
    p.currentOutput = fake.random_int(min=0, max=9999, step=1)
    return p
