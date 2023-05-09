class Coffee:
    def __init__(self, name):
        self.name = name
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def set_name(self, name):
        self._name = name
        
        if type(name) == str and not hasattr(self, 'name'):
            self._name = name
        else:
            raise Exception('Name is not a string.')


    def orders(self, new_order=None):
        from classes.order import Order
        pass
    
    def customers(self, new_customer=None):
        from classes.customer import Customer
        pass
    
    def num_orders(self):
        pass
    
    def average_price(self):
        pass