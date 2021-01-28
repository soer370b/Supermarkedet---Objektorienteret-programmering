import sqlite3
from logiklag import Productgroup, Product
import Data_stregkode_vare_base
<<<<<<< HEAD

print('Starter')
con = sqlite3.connect('database.db')
print('Database åbnet')

=======
>>>>>>> 817dfa1bc07ea913e5859d1fbb0ed71a4c5b38eb

class Data:
    def __init__(self):
        print('Starter')
        self.con = sqlite3.connect('database.db')
        print('Database åbnet')
        try:
            self.con.execute("""CREATE TABLE productgroups (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name STRING)""")
<<<<<<< HEAD
            con.execute("""CREATE TABLE products (
                id INTEGER PRIMARY KEY AUTOINCREMENT, productid INTEGER, PLU INTEGER,
                id INTEGER PRIMARY KEY AUTOINCREMENT, productid INTEGER,
=======
            self.con.execute("""CREATE TABLE products (
                id INTEGER PRIMARY KEY AUTOINCREMENT, productid INTEGER, PLU INTEGER,
>>>>>>> 817dfa1bc07ea913e5859d1fbb0ed71a4c5b38eb
                name STRING, price FLOAT, productgroup INTEGER,
                purchaseprice FLOAT, location STRING)""")
            print('Tabellen er oprettet')
        except Exception as e:
            print('Tabellen er åben')
            print(e)
<<<<<<< HEAD
    # def new_productgroup(self, name):
    #     c = con.cursor()
    #     c.execute('SELECT name FROM productgroups WHERE name = ? ', (name,))
    #     a = c.fetchone()
    #     if a[0] != name:
    #         Productgroup.name = name
    #         c = con.cursor()
    #         c.execute('INSERT INTO productgroups (name) VALUES (?)', (Productgroup.name,))
    #         con.commit()
=======
        self.con.commit()
>>>>>>> 817dfa1bc07ea913e5859d1fbb0ed71a4c5b38eb

    def new_productgroup(self, name):
        c = self.con.cursor()
        c.execute('SELECT name FROM productgroups WHERE name = ? ', (name,))
        a = c.fetchone()
        if a == None:
            c = self.con.cursor()
            c.execute('INSERT INTO productgroups (name) VALUES (?)', (name,))
            self.con.commit()

    def edit_productgroup(self, id, newname):
        c = self.con.cursor()
        c.execute('UPDATE productgroups SET name = (?) WHERE id = (?)', (newname, id))
        self.con.commit()

    def delete_productgroup(self, id):
        c = self.con.cursor()
        c.execute('DELETE FROM productgroups WHERE id = (?)', (id,))
<<<<<<< HEAD
    def edit_productgroup(self, name, newname):
        c = con.cursor()
        c.execute('UPDATE productgroups SET name = (?) WHERE name = (?)', (newname, name))
        con.commit()

    def delete_productgroupe(self, name):
        c = con.cursor()
        c.execute('DELETE FROM productgroups WHERE name = (?)', (name,))
        con.commit()
=======
        self.con.commit()
>>>>>>> 817dfa1bc07ea913e5859d1fbb0ed71a4c5b38eb

    def get_productgroups(self):
        id = []
        name = []
        productgroups = []
<<<<<<< HEAD
        c = con.cursor()
=======
        c = self.con.cursor()
>>>>>>> 817dfa1bc07ea913e5859d1fbb0ed71a4c5b38eb
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

    def new_product(self, name, productid, PLU, price, productgroup, purchaseprice, location):
        def productgroup_chek(productgroup):
            cheker = False
            pg = self.get_productgroups()
            for i in pg:
                if i.name == productgroup:
                    cheker = True
            return cheker

        type(productid)
        if productid == '':
            productid = Data_stregkode_vare_base.get_barcode_code()
            print(productid)

        elif len(productid) == 13:
            print(productid)

        elif len(productid) != 13:
            print('ikke valid stregkode, ny generet')
            print('gammel stegkode: ' + productid)
            productid = Data_stregkode_vare_base.get_barcode_code()
            print('ny stegkode: ' + productid)

        if productgroup_chek(productgroup) == True:
            if PLU == '':
                c = self.con.cursor()
                c.execute('''INSERT INTO products (name, productid, price,
                            productgroup, purchaseprice,
                            location) VALUES (?, ?, ?, ?, ?, ?)''', (name,
                            productid, price, productgroup,
                            purchaseprice, location, ))
                self.con.commit()

            else:
                c = self.con.cursor()
                c.execute('''INSERT INTO products (name, productid, PLU, price,
                            productgroup, purchaseprice,
                            location) VALUES (?, ?, ?, ?, ?, ?, ?)''', (name,
                            productid, PLU, price, productgroup,
                            purchaseprice, location, ))
                self.con.commit()
        else:
            print('Produktgruppen findes ikke!')

if __name__ == "__main__":
    Data = Data()
    name = 'Øl'
    id = '254889541835'
    PLU = '654'
    price = 10
    productgroup = 'Frost'
    pprice = 5
    location = 'Frost'
    Data.new_product(name, id, PLU, price, productgroup, pprice, location)

'''
    data = Data()
    name = 'Fisk'
    data.new_productgroup(name)
    a = data.get_productgroups()

    for p in a:
        print(p.id, p.name)
'''
<<<<<<< HEAD
            # print('Id = ' + pid)
            pname = str(data[i][1])
            # print('Navn = ' + pname + '\n')
            id.append(pid)
            name.append(pname)
        list = [id, name]
        return list

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
    data.get_productgroups()
=======
>>>>>>> 817dfa1bc07ea913e5859d1fbb0ed71a4c5b38eb
