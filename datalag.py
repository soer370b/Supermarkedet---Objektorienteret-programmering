import sqlite3
from logiklag import Productgroup
print('Starter')
con = sqlite3.connect('database.db')
print('Database åbnet')


class Data:
    def __init__(self):

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

    # def new_productgroup(self, name):
    #     c = con.cursor()
    #     c.execute('SELECT name FROM productgroups WHERE name = ? ', (name,))
    #     a = c.fetchone()
    #     if a[0] != name:
    #         Productgroup.name = name
    #         c = con.cursor()
    #         c.execute('INSERT INTO productgroups (name) VALUES (?)', (Productgroup.name,))
    #         con.commit()

    def new_productgroup(self, name):
        c = con.cursor()
        c.execute('SELECT name FROM productgroups WHERE name = ? ', (name,))
        a = c.fetchone()
        if a == None:
            c = con.cursor()
            c.execute('INSERT INTO productgroups (name) VALUES (?)', (name,))
            con.commit()

    def edit_productgroup(self, id, newname):
        c = con.cursor()
        c.execute('UPDATE productgroups SET name = (?) WHERE id = (?)', (newname, id))
        con.commit()

    def delete_productgroup(self, id):
        c = con.cursor()
        c.execute('DELETE FROM productgroups WHERE id = (?)', (id,))
        con.commit()

    def get_productgroups(self):
        id = []
        name = []
        productgroups = []
        c = con.cursor()
        c.execute('SELECT * FROM productgroups')
        data = c.fetchall()
        print('Der er ' + str(len(data)) + ' produktgrupper')
        for i in range(len(data)):
            pid = str(data[i][0])
            print('Id = ' + pid)
            pname = str(data[i][1])
            print('Navn = ' + pname + '\n')
            p = Productgroup(pid, pname)
            productgroups.append(p)
        return productgroups

    def new_product(self, name, productid, price, productgroup, purchaseprice, location):
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


if __name__ == "__main__":
    data = Data()
    name = 'Fisk'
    data.new_productgroup(name)
    a = data.get_productgroups()

    for p in a:
        print(p.id, p.name)
