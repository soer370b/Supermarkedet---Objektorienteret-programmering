'''

Krav til programmet:
Skal bygges på en dynamisk database
Skal kunne indholde produkter som fx. navn og kategori
Skal kunne lave stregkoder af typen EAN-13
Skal kunne læse stregkoder af EAN-13 typen i billedeformat
    det skal så kunne finde data til det tilhørende produkt fra databasen ud fra scanningen
Skal kunne vise grafisk aflæsningen af EAN-13 stregkoder

'''





import math
import uuid
import random
import sqlite3
import barcode
from barcode.writer import ImageWriter
from pyzbar import pyzbar
from PIL import Image
import os
import numpy as np
import matplotlib.pyplot as plt

dirname = os.path.dirname(__file__)

print('Starter')
con = sqlite3.connect('database.db')
print('Database åbnet')

try:
    con.execute("""CREATE TABLE data (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        navn STRING, kategori STRING, idgen STRING, bacode INTEGER)""")
    print('Tabellen er oprettet')
except Exception as e:
    print('Tabellen er åben')

def get_id():
    id = uuid.uuid4()
    return id
# id = get_id()

def get_barcode_code():
    hele_tal = 0
    Ulige_tal = 0
    tal_list = []

    for i in range(0,12):
        tal = random.randint(0,9)
        if i%2 == 0:
            hele_tal += tal
        else:
            Ulige_tal += tal
        tal_list.append(str(tal))

    print(tal_list)
    print("__________________________________________________")
    print(hele_tal)
    print("__________________________________________________")
    print(Ulige_tal)
    print("__________________________________________________")

    appen_tal = (3*Ulige_tal)+hele_tal

    while appen_tal%10 != 0:
        appen_tal +=1
    print(str(appen_tal-((3*Ulige_tal)+hele_tal)))
    tal_list.append(str(appen_tal-((3*Ulige_tal)+hele_tal)))

    s = ''.join(tal_list)
    print("__________________________________________________")
    print(s)
    return(s)

def Ean_writer(t, n):
    EAN = barcode.get_barcode_class('ean13')
    ean = EAN(u'{}'.format(t), writer=ImageWriter())
    fullname = ean.save('{}'.format(n))

# def reader():
#     b = str()
#     filename = os.path.join(dirname,"/Users/thomas/b")
#     info = pyzbar.decode(Image.open(os.path.join(dirname,"")))
# c = con.cursor()
# c.execute('INSERT INTO data (navn, kategori, idgen) VALUES (?, ?, ?)',('Lenovo', 'Computer', str(id)))
# con.commit()
inp = ''

print('')
print('Kommandoer: ')
print('ny           - Opretter en ny genstand')
print('list         - Viser en liste over genstande i databasen')
print('delete       - Sletter en genstand eller en kategori')
print('rediger      - Redigerer den data for valgte ting')
print('stregkode    - Laver en EAN-13 ud fra GTIN-13 nummer')
print('scan         - Læser det valgte billede med stregkode')
print('handlinger   - Viser en liste over Kommandoer')
print('quit         - Programmet lukkes')

while not inp.startswith('quit'):
    inp = input('> ')

    if inp == 'test':
        print('test')

    elif inp == 'ny':
        n = input('Indtast ting: ')
        k = input('Indtast kategori: ')
        getid = get_id()
        b = get_barcode_code()
        c = con.cursor()
        c.execute('INSERT INTO data (navn, kategori, idgen, bacode) VALUES (?, ?, ?, ?)',(n, k, str(getid), int(b)))
        con.commit()

    elif inp == 'list':
        c = con.cursor()
        c.execute('SELECT navn, kategori, bacode FROM data')

        for p in c:
            print('Ting: {}, Kategori: {}, Stregkode: {}'.format(p[0], p[1], p[2]))

    elif inp == 'delete':
        print('Indtast den valgte kolonne: ')
        print('Kommandoer: ')
        print('ting - vælg en ting')
        print('kategori - slet en hel kategori')
        inp = input('>  ')
        if inp == 'ting':
            t = input('Indtast ting: ')
            try:
                c = con.cursor()
                c.execute('DELETE FROM data WHERE navn = ?', [t])
                con.commit()
                print(t + ' slettet')
            except:
                print('Fejl')
        if inp == 'kategori':
            k = input('Indtast kategori: ')
            try:
                c = con.cursor()
                c.execute('DELETE FROM data WHERE kategori = ?', [k])
                con.commit()
                print('Kategorien ' + k + ' er slettet')
            except:
                print('Fejl')

    elif inp == 'rediger':
        print('Listen viser ID\'et. Det ID skal bruges når der skal redigers i data.')
        c = con.cursor()
        c.execute('SELECT id, navn, kategori FROM data')

        for p in c:
            print('ID: {}, Navn: {}, Kategori: {}'.format(p[0], p[1], p[2]))
        id = input('Indtast ID\'et: ')
        n = input('Indtast nyt navn: ')
        k = input('Indtast ny kategori: ')
        c = con.cursor()
        c.execute('UPDATE data SET navn = ?, kategori = ? WHERE id = ?', [n, k, id])
        con.commit()
        print('Rettelse gemt')

    elif inp == 'stregkode':
        i = input('Indtast ting: ')
        c = con.cursor()
        h = c.execute('SELECT bacode FROM data WHERE navn = ?', [i])
        con.commit()
        for p in c:
            t = p[0]
            print('Stregkoden til ' + str(i) + ' er ' + str(t))
        if __name__ == '__main__':
            n = i
            Ean_writer(t, n)
            print('Stregkode lavet')

    elif inp == 'barcode':
        b = barcode.get_barcode_code()
        print(b)

    elif inp == 'handlinger':
        print('Kommandoer: ')
        print('ny           - Opretter en ny genstand')
        print('list         - Viser en liste over genstande i databasen')
        print('delete       - Sletter en genstand eller en kategori')
        print('rediger      - Redigerer den data for valgte ting')
        print('stregkode    - Laver en EAN-13 ud fra GTIN-13 nummer')
        print('scan         - Læser det valgte billede med stregkode')
        print('handlinger   - Viser en liste over Kommandoer')
        print('quit         - Programmet lukkes')


    elif inp == 'scan':
        try:
            i = input('Indtast billede navn: ')
            #filename = os.path.join(dirname,i+".png")
            #info = pyzbar.decode(Image.open(os.path.join(dirname,i+".png")))
            i = i+".png"
            print("scanner: " + i)

            #### viser scanningen med RGB analysering ####
            image_path = i
            img = Image.open(image_path)
            width, height = img.size
            basewidth = 4*width
            img = img.resize((basewidth, height), Image.ANTIALIAS)
            hor_line_bw = img.crop((0, int(height/2), basewidth, int(height/2) + 1)).convert('L')
            hor_data = np.asarray(hor_line_bw, dtype="int32")[0]

            hor_data = 255 - hor_data
            avg = np.average(hor_data)
            # plt.ion()
            plt.plot(hor_data)
            plt.show(block=False)

            info = pyzbar.decode(Image.open(i))
            # print(info)
            test = info[0]
            data9 = test[0]
            # q = int(len(data9)-1)
            # counter = 2
            print('__________________________________________________')
            print(test)
            print(data9)
            #stregkode_nummer = data9[:1:] + data9[:2:] + data9[:-1:]
            stregkode_nummer = int(data9[:13:])
            print(stregkode_nummer)
            print('__________________________________________________')

            c = con.cursor()
            find_produkt = c.execute('SELECT navn, kategori, bacode FROM data WHERE bacode = ?',(stregkode_nummer,))
            for p in c:
                print('Ting: {}, Kategori: {}, Stregkode: {}'.format(p[0], p[1], p[2]))
        except:
            print('Fejl ved scanning')

'''
Efter man har oprettet en ny ting,
skal man genstarte programmet før man kan lave en stregkode som billede.
'''
