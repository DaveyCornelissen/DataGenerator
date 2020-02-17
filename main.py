from faker import Faker
import json
import csv
import pandas as pd 
import numpy as np 
from classes.Customer import Customer
from classes.Producers import Producers

fake = Faker('nl_NL')
data = []
fileName = ""
# csvFile = open("Customers.csv", "w")


# fieldnames = ['first_name','last_name']
# writer = csv.DictWriter(csvFile, fieldnames=fieldnames)
# writer.writeheader()

def generateFaker(self, type=''):
    
    if type == 'c':
        fileName = "Customers.json"
        c = Customer()
        c.id = fake.random_int(min=0, max=99999999, step=1)
        c.name = fake.name()
        c.adress = fake.address()
        return c
    elif type == 'p':
        fileName = "Producers.json"
        p = Producers()
        p.id = fake.random_int(min=0, max=99999999, step=1)
        p.name = fake.company()
        p.adress = fake.address()
        p.currentOutput = fake.random_int(min=0, max=9999, step=1)
        return p


for _ in range(1000):
    data.append(generateFaker("p"))
    # writer.writerow(c.__dict__)
    
print("generating done! Total of {o} objects created".format(o=len(data)))

print(fileName)
jsonFile = open(fileName, "w")
jsonFile.writelines(json.dumps([c.__dict__ for c in data]))
jsonFile.close()

    


