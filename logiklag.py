import datetime

class Product():
    def __init__(self, id, name, price, pprice, location):
        self.productid = id
        self.name = name
        self.price = price
        # self.productgroup = Productgroup
        self.purchasedate = datetime.date()
        self.purchaseprice = pprice
        self.location = location

class Productgroup():
    def __init__(self, id, name):
        self.id = id
        self.name = name

class ProductID():
    def __init__(self, type):
        if type == 'EAN13':
            print('EAN13')
        if type == 'PLU':
            print('PLU')
