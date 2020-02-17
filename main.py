import json
import time
from services.MockService import *
import os
 
dirpath = os.getcwd()
fileName = ""


#waiting for input

print('Welcome to the Mock generator for the Energy Grid!')

time.sleep(2)

dataType = input('Choose your mock dataType: P = Producers / C = Customers: ')

time.sleep(1)

amount = input('Fill in the amount of mock data row: ')

time.sleep(1)

fileName = input('Choose your file name (can leave default): ')

if fileName == '' and dataType == 'P':
    fileName = "Producers.json"
elif fileName == '' and dataType == 'C':
    fileName = "Customers.json"

time.sleep(1)

directory = input('Fill in the file directory (can leave default): ')

time.sleep(1)

print('Great! Lets start mocking!')

mockData = Generate(dataType, int(amount))

print("generating done! Total of {o} objects created".format(o=len(mockData)))

fullpath = ''

if directory != '':
    fullPath = directory + '/' + fileName
else :
    fullPath = dirpath + '/' + fileName

# csvFile = open("Customers.csv", "w")
# fieldnames = ['first_name','last_name']
# writer = csv.DictWriter(csvFile, fieldnames=fieldnames)
# writer.writeheader()

jsonFile = open(fullPath, "w")
jsonFile.writelines(json.dumps([c.__dict__ for c in mockData]))
jsonFile.close()
