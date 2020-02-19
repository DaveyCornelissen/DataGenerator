import json
import time
from services.MockService import *
import os
import csv
import itertools
import threading
import time
import sys

dirpath = os.getcwd()
fileName = ""


# waiting for input

print('Welcome to the Mock generator for the Energy Grid!')

time.sleep(2)

dataType = input('Choose your mock dataType: P = Producers / C = Customers: ')

if dataType != 'P' and dataType != 'C':
    print('invalid dataType! exiting...')
    quit()

amount = input('Fill in the amount of mock data row: ')

res = isinstance(amount, int)

if amount == '':
    print('invalid amount! exiting...')
    quit()

if int(amount) < 1:
    print('invalid amount! exiting...')
    quit()

fileName = input(
    'Choose your file name (can leave default)! no need to specify the file type: ')

if fileName == '' and dataType == 'P':
    fileName = "Producers"
elif fileName == '' and dataType == 'C':
    fileName = "Customers"

if fileName.find('.') != -1:
    index = fileName.index('.')
    if len(fileName) > index:
        fileName = fileName[0: index:] + fileName[len(fileName) + 1::]

print('Choose file type: json / csv')

time.sleep(0.5)

fileType = input('Select options: ')

if (fileType != 'json' and fileType != 'csv'):
    print('No valid file type provided! Exiting...')
    quit()

if fileType.find('.') != -1:
    fileType.replace('.', '')

fileName = fileName + '.' + fileType

directory = input('Fill in the file directory (can leave default): ')

fullpath = ''

if directory != '':
    fullPath = directory + '\\' + fileName
else:
    fullPath = dirpath + '\\' + fileName

print('Great! Lets start mocking!')

time.sleep(1)

elapsedtime = 0
done = False


def animate():
    global elapsedtime
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if done:
            break
        sys.stdout.write('\rGenerating mock data! ' + c)
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write('\rgenerating done! Total of {o} objects created in {t} seconds   '.format(
        o=len(mockData), t=elapsedtime))


t = threading.Thread(target=animate)
start = time.time()
t.start()
mockData = Generate(dataType, int(amount))

if fileType == 'csv':
    csvFile = open(fullPath, "w")
    writer = csv.writer(csvFile)

    model = type(mockData[0])
    csvHeaders = model.headers


    writer.writerow(csvHeaders)

    for cdr in mockData:
        writer.writerow(list(cdr))
    csvFile.close()
elif fileType == 'json':
    jsonFile = open(fullPath, "w")
    jsonFile.writelines(json.dumps([c.__dict__ for c in mockData]))
    jsonFile.close()

elapsedtime = time.time() - start
elapsedtime = str(round(elapsedtime, 2))
done = True
