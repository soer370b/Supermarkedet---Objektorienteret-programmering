import datetime

class Product():
    def __init__(self, id, pid, PLU, name, price, productgroup, pprice, location):
        self.id = id
        self.pid = pid
        self.plu = PLU
        self.name = name
        self.price = price
        self.productgroup = productgroup
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
