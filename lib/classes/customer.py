class Customer:
    def __init__(self, name):
        self.name = name
        
    @property
    def name(self):
        return self._name
    
    @name.setter
    def set_name(self, name):
        self._name = name
        
        if type(name) == str and len(name) >= 1 and len(name) <= 15 and not hasattr(self, 'name' ):
            self._name = name
        else:
            raise Exception('Name is not between 1 to 15 characters.')

    def orders(self, new_order=None):
        from classes.order import Order
        
    
    def coffees(self, new_coffee=None):
        from classes.coffee import Coffee
        pass