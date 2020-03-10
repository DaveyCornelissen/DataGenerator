class Customer:
    Headers = ['id', 'name', 'adress']
    CustomerId = 0
    Name = ''
    Street = ''
    City = ''
    Postcode = ''
    Energy = ''

    def __init__(self, CustomerId=0, Name = '', Street = '', City = '', Postcode = '', Energy = ''):
        self.CustomerId = CustomerId
        self.Name = Name
        self.Street = Street
        self.City = City
        self.Postcode = Postcode
        self.Energy = Energy

    # def __iter__(self):
    #     return iter([self.id, self.name, self.adress])
        
