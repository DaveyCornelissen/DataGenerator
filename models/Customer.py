class Customer:
    def __init__(self, number=0, name='', adress=''):
        self.id = number
        self.name = name
        self.adress = adress

    def __iter__(self):
        return iter([self.id, self.name, self.adress])
        
