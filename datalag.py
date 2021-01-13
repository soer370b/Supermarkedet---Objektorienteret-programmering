import sqlite3
from logiklag import Product, Productgroup, ProductID

print('Starter')
con = sqlite3.connect('database.db')
print('Database åbnet')

try:
    con.execute("""CREATE TABLE productgroups (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name STRING)""")
    con.execute("""CREATE TABLE products (
        id INTEGER PRIMARY KEY AUTOINCREMENT, productid INTEGER,
        name STRING, price FLOAT, productgroup INTEGER,
        purchaseprice FLOAT, location STRING)""")
    print('Tabellen er oprettet')
except Exception as e:
    print('Tabellen er åben')
    print(e)

# def new_productgroup(name):
#     c = con.cursor()
#     c.execute('SELECT name FROM productgroups WHERE name = ? ', (name,))
#     a = c.fetchone()
#     if a[0] != name:
#         Productgroup.name = name
#         c = con.cursor()
#         c.execute('INSERT INTO productgroups (name) VALUES (?)', (Productgroup.name,))
#         con.commit()

def new_productgroup(name):
    Productgroup.name = name
    c = con.cursor()
    c.execute('INSERT INTO productgroups (name) VALUES (?)', (Productgroup.name,))
    con.commit()

def new_product(name, productid, price, productgroup, purchaseprice, location):
    Product.name = name
    Product.productid = productid
    Product.price = price
    Product.productgroup = productgroup
    # Product.purchasedate = purchasedate
    Product.purchaseprice = purchaseprice
    Product.location = location

    c = con.cursor()
    c.execute('''INSERT INTO products (name, productid, price,
                productgroup, purchaseprice,
                location) VALUES (?, ?, ?, ?, ?, ?)''', (Product.name,
                Product.productid, Product.price, Product.productgroup,
                Product.purchaseprice, Product.location, ))
    con.commit()
#note Der mangler en datetime i varekolonnen.

# name = 'Mejeri'
#
# new_productgroup(name)

pname = 'Ost'
pid = 1235
price = 50
ppgroup = 3
ppprice = 25
plocation = 'Køledisk'

new_product(pname, pid, price, ppgroup, ppprice, plocation)

PLU = 'PLU'

ProductID.PLU = PLU
