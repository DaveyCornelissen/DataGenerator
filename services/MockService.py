from faker import Faker
from models.Customer import *
from models.Producers import *
from models.Energy import *

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
    c.CustomerId = fake.random_int(min=0, max=99999999, step=1)
    c.Name = fake.name()
    c.Street = fake.street_name()
    c.City = fake.city()
    c.Postcode = fake.postcode()
    return c

def __MockProducers():
    p = Producers()
    p.id = fake.random_int(min=0, max=99999999, step=1)
    p.name = fake.company()
    p.adress = fake.address()
    p.currentOutput = fake.random_int(min=0, max=9999, step=1)
    return p

def __MockEnergy():
    e = Energy()
    e.ID = fake.random_int(min=0, max=99999999, step=1)
    e.KiloWattperHour = fake.random_int(min=0, max=9999, step=5)
    e.Date = fake.unix_time(end_datetime=None, start_datetime=None)
    return e