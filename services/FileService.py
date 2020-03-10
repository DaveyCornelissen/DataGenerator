import os
import csv
import json
import itertools

Path = ''
Data = []
FileName = ''
Extension = ''
dirpath = os.getcwd()

def GenerateFile(data):
    global Extension
    if Extension == 'csv':
        __GenerateCSV(data)
    elif Extension == 'json':
        __GenerateJSON(data)

def SelectExtension():
    global FileName
    Extension = input('Select options: ')

    if (Extension != 'json' and Extension != 'csv'):
        print('No valid file type provided! Exiting...')
        quit()

    if Extension.find('.') != -1:
        Extension.replace('.', '')

    FileName = FileName + '.' + Extension


def SetDirectory():
    global Path
    global FileName
    global dirpath
    directory = input('Fill in the file directory (can leave default): ')

    if directory != '':
        Path = directory + '\\' + FileName
    else:
        Path = dirpath + '\\' + FileName

def DefineFileName(dataType): 
    FileName = input(
        'Choose your file name (can leave default)! no need to specify the file type: ')

    if FileName == '' and dataType == 'P':
        FileName = "Producers"
    elif FileName == '' and dataType == 'C':
        FileName = "Customers"

    if FileName.find('.') != -1:
        index = FileName.index('.')
        if len(FileName) > index:
            FileName = FileName[0: index:] + FileName[len(FileName) + 1::]


def __GenerateCSV(data):
    global Path
    csvFile = open(Path, "w")
    writer = csv.writer(csvFile, lineterminator='\n')

    model = type(data[0])
    csvHeaders = model.headers
    writer.writerow(csvHeaders)

    for cdr in data:
        writer.writerow(list(cdr))
    csvFile.close()


def __GenerateJSON(data):
    global Path
    jsonFile = open(Path, "w")
    jsonFile.writelines(json.dumps([c.__dict__ for c in data]))
    jsonFile.close()
