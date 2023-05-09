
class Order:

    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price

    @property
    def price(self):
        return self._price
    
    @price.setter
    def set_price(self, price):
        self._price = price
        
        if type(price) == (int or float) and price >= 1 and price <= 10 and not hasattr(self, price):
            self._price = price
        else:
            raise Exception('Price must be a number.')

