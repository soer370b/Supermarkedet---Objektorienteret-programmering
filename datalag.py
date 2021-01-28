import sqlite3
from logiklag import Productgroup, Product
import Data_stregkode_vare_base
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
                id INTEGER PRIMARY KEY AUTOINCREMENT, productid INTEGER, PLU INTEGER,
                name STRING, price FLOAT, productgroup INTEGER,
                purchaseprice FLOAT, location STRING)""")
            print('Tabellen er oprettet')
        except Exception as e:
            print('Tabellen er åben')
            print(e)

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

    def new_product(self, name, productid, PLU, price, productgroup, purchaseprice, location):
        def productgroup_chek(productgroup):
            cheker = False
            pg = Data.get_productgroups()
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
                c = con.cursor()
                c.execute('''INSERT INTO products (name, productid, price,
                            productgroup, purchaseprice,
                            location) VALUES (?, ?, ?, ?, ?, ?)''', (name,
                            productid, price, productgroup,
                            purchaseprice, location, ))
                con.commit()

            else:
                c = con.cursor()
                c.execute('''INSERT INTO products (name, productid, PLU, price,
                            productgroup, purchaseprice,
                            location) VALUES (?, ?, ?, ?, ?, ?, ?)''', (name,
                            productid, PLU, price, productgroup,
                            purchaseprice, location, ))
                con.commit()
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
