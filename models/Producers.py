class Producers:
    headers = ['id', 'name', 'adress', 'currentOutput']

    def __init__(self, name='', adress='', currentOutput=''):
        self.id = id
        self.name = name
        self.adress = adress
        self.currentOutput = currentOutput
    
    def __iter__(self):
        return iter([self.id, self.name, self.adress, self.currentOutput])

           