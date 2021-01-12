import sqlite3
from logiklag import Product, Productgroup

print('Starter')
con = sqlite3.connect('database.db')
print('Database åbnet')

try:
    con.execute("""CREATE TABLE productgroups (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name STRING)""")
    print('Tabellen er oprettet')
except Exception as e:
    print('Tabellen er åben')
    print(e)

def new_productgroup(name):
    Productgroup.name = name
    c = con.commit()
    c.execute('INSERT INTO productgroups (name) VALUES (?)', (Productgroup.name))

def new_product(productid, name, price, productgroup, purchasedate, purchaseprice, location):
    pass

name = 'Frost'

new_productgroup(name)
