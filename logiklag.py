import datetime

class Product():
    def __init__(self, productgroup):
        self.productid = 0
        self.name = ''
        self.price = 0
        self.productgroup = productgroup
        self.purchasedate = datetime.date()
        self.purchaseprice = 0
        self.location = ''

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
