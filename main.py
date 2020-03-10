from services import MockService
from services import FileService
import itertools
from Utils import LoadingThread


# waiting for input
print('Welcome to the Mock generator for the Energy Grid!')

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

FileService.DefineFileName(dataType)
FileService.SetDirectory()
FileService.SelectExtension()

LoadingThread.start()
mockData = MockService.Generate(dataType, int(amount))
LoadingThread.mockData = mockData

FileService.GenerateFile(mockData)
LoadingThread.stop()
