import datetime

class Product():
    def __init__(self):
        self.productid = 0
        self.name = ''
        self.price = 0
        self.productgroup = ''
        self.purchasedate = datetime.date()
        self.purchaseprice = 0
        self.location = ''

class Productgroup():
    def __init__(self):
        # self.id = 0
        self.name = ''

class ProductID(type):
    def __init__(self):
        if type == 'EAN13':
            print('EAN13')
        if type == 'PLU':
            print('PLU')
