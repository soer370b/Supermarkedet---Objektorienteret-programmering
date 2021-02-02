import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
import numpy as np
from logiklag import *
from datalag import *
from PIL import ImageTk, Image
import os
print("Import complete")

dirname = os.path.dirname(__file__)

filename = os.path.join(dirname,"growingstore.png")

infile = open(filename, mode='r', encoding="utf8")

class Main(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.logo_logo()
    def logo_logo(self):
        img = Image.open(os.path.join(dirname,"growingstore.png"))
        infile = open(filename, mode='r', encoding="utf8")
        img = img.resize((300, 150), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(img.convert("RGB"))
        self.logo = tk.Label(self, image=img)
        self.logo.image = img
        #self.logo.image = img
        # self.logo.grid(column =x, row = y)

        self.Data = Data()
        # self.Product = Product()

        self.buttons = []
        for i in range(6):
            self.buttons.append(tk.Button(self))
        # self.main = tk.Frame(self)

        self.logo.grid(row=0, column=0, rowspan=2)
        self.varegruppe = self.buttons[0]
        self.varegruppe["text"] = "Varegruppe"
        self.varegruppe["command"] = self.varegrup
        self.varer = self.buttons[1]
        self.varer['text'] = 'Varer'
        self.varer['command'] = self.products
        self.test_tabel = self.buttons[4]
        self.test_tabel['text'] = 'Opdater tabel TEST (productgroups)'
        self.test_tabel['command'] = self.update_productgroup_tabel
        self.log_ud = self.buttons[5]
        self.log_ud['text'] = 'Log ud'
        self.log_ud['command'] = self.log__ud
        self.buttons[0].grid(row=2, column=0, sticky="nsew")
        self.buttons[1].grid(row=3, column=0, sticky="nsew")
        self.buttons[2].grid(row=4, column=0, sticky="nsew")
        self.buttons[3].grid(row=5, column=0, sticky="nsew")
        self.buttons[4].grid(row=6, column=0, sticky="nsew")
        self.buttons[5].grid(row=7, column=0, sticky="nsew")
        self.grid(row=2, column=2, columnspan=2, rowspan=6)

# Productgroup
    def update_productgroup_tabel(self):
        l = self.Data.get_productgroups()

        self.tree.delete(*self.tree.get_children())
        for p in l:
            id = int(p.id)
            name = str(p.name)
            print(id)
            print(name)
            self.tree.insert("", 0 , values=(id, name))
        self.tree.heading("#1", text="Produktgrupper")

    def varegrup(self):
        print('Varegruppeside')
        self.productgroup_Window()

    def log__ud(self):
        print('Log ud')

    def select_item(self, data):
        item = self.tree.focus()
        dic = self.tree.item(item)

    def log__ud(self):
        print('Log ud')

    def productgroup_Window(self):
        def close():
            self.productgroupWindow.destroy()
            self.productgroupWindow.update()

        self.productgroupWindow = tk.Toplevel()
        self.productgroupWindow.geometry("1080x720")
        self.productgroupWindow.grab_set()
        self.productgroupWindow.wm_title('Varegrupper')

        self.back = tk.Button(self.productgroupWindow, text = 'Tilbage')
        self.back['command'] = close
        self.back.grid(row=0, column=1, sticky="nsew")

        self.newproductgroup = tk.Button(self.productgroupWindow, text = 'Ny varegruppe')
        self.newproductgroup['command'] = self.createnewproductgroup
        self.newproductgroup.grid(row=1, column=1, sticky="nsew")

        self.editproductgroup = tk.Button(self.productgroupWindow, text = 'Ret varegruppe')
        self.editproductgroup['command'] = self.edit_productgroup_
        self.editproductgroup.grid(row=2, column=1, sticky="nsew")

        self.deleteproductgroup = tk.Button(self.productgroupWindow, text = 'Slet varegruppe')
        self.deleteproductgroup['command'] = self.delete_productgroup_
        self.deleteproductgroup.grid(row=3, column=1, sticky="nsew")


        self.tree = ttk.Treeview(self.productgroupWindow, columns=("Id", "Name"), show = 'headings')
        self.tree.heading("#1", text="Produktgrupper")
        self.tree['displaycolumns'] = ('Name')
        self.tree.bind('<ButtonRelease-1>', self.select_item)
        self.update_productgroup_tabel()
        self.tree.grid(row=0, rowspan=4, column = 2)

    def createnewproductgroup(self):
        def close():
            self.create_newproductgroup.destroy()
            self.create_newproductgroup.update()
        def save_data():
            name = str(self.pgroup_input.get())
            self.Data.new_productgroup(name)
            close()
            self.update_productgroup_tabel()
        self.create_newproductgroup = tk.Toplevel()
        self.create_newproductgroup.geometry("1080x720")
        self.create_newproductgroup.grab_set()
        self.create_newproductgroup.wm_title('Ny produktgruppe')
        self.save_nprodutg = tk.Button(self.create_newproductgroup, text = 'Gem varegruppe')
        self.save_nprodutg['command'] = save_data
        self.save_nprodutg.grid(column=1, sticky="nsew")
        self.back_nprodutg = tk.Button(self.create_newproductgroup, text = 'Tilbage')
        self.back_nprodutg['command'] = close
        self.back_nprodutg.grid(column=1, sticky="nsew")
        tk.Label(self.create_newproductgroup, text='Indsæt produktgruppen: ').grid(row=0, column=2)
        self.pgroup_input = tk.Entry(self.create_newproductgroup)
        self.pgroup_input.grid(row=1, column=2)

    def edit_productgroup_(self):
        def close():
            self.create_newproductgroup.destroy()
            self.create_newproductgroup.update()

        def get_item():
            item = self.tree.focus()
            dic = self.tree.item(item)
            list = dic.get('values')
            id = list[0]
            navn = list[1]
            return id, navn

        def edit_pgroup():
            new_name = self.epgroup_input.get()
            print(type(old_id))
            self.Data.edit_productgroup(old_id, new_name)
            self.update_productgroup_tabel()
            close()

        self.create_newproductgroup = tk.Toplevel()
        self.create_newproductgroup.geometry("1080x720")
        self.create_newproductgroup.grab_set()
        self.create_newproductgroup.wm_title('Ret varegruppe')

        old_id, old_item = get_item()

        self.back_nprodutg = tk.Button(self.create_newproductgroup, text = 'Tilbage')
        self.back_nprodutg['command'] = close
        self.back_nprodutg.grid(column=1, sticky="nsew")

        self.save_nprodutg = tk.Button(self.create_newproductgroup, text = 'Gem varegruppe')
        self.save_nprodutg.grid(column=1, sticky="nsew")
        self.save_nprodutg['command'] = edit_pgroup

        tk.Label(self.create_newproductgroup, text='Den valgte produktgruppe er: {}'.format(old_item)).grid(row=0, column=2)
        tk.Label(self.create_newproductgroup, text='Indtast rettelse: ').grid(row=1, column=2)

        self.epgroup_input = tk.Entry(self.create_newproductgroup)
        self.epgroup_input.grid(row=1, column=3)

    def delete_productgroup_(self):
        def close():
            self.create_newproductgroup.destroy()
            self.create_newproductgroup.update()

        def get_item():
            item = self.tree.focus()
            dic = self.tree.item(item)
            list = dic.get('values')
            id = list[0]
            navn = list[1]
            return id, navn

        def delete_pgroup():
            self.Data.delete_productgroup(id)
            self.update_productgroup_tabel()
            close()

        self.create_newproductgroup = tk.Toplevel()
        self.create_newproductgroup.geometry("1080x720")
        self.create_newproductgroup.grab_set()
        self.create_newproductgroup.wm_title('Slet varegruppe')

        id, item = get_item()

        self.back_nprodutg = tk.Button(self.create_newproductgroup, text = 'Tilbage')
        self.back_nprodutg['command'] = close
        self.back_nprodutg.grid(column=1, sticky="nsew")

        self.save_nprodutg = tk.Button(self.create_newproductgroup, text = 'Slet varegruppe')
        self.save_nprodutg.grid(column=1, sticky="nsew")
        self.save_nprodutg['command'] = delete_pgroup

        tk.Label(self.create_newproductgroup, text='Den valgte produktgruppe er: {}'.format(item)).grid(row=0, column=2)

#products
    def update_product_tabel(self):
        l = self.Data.get_products()

        self.tree.delete(*self.tree.get_children())
        for p in l:
            id = int(p.id)
            pid = int(p.pid)
            PLU = p.plu
            name = str(p.name)
            price = float(p.price)
            productgroup = str(p.productgroup)
            pprice = float(p.purchaseprice)
            location =  str(p.location)
            self.tree.insert("", 0 , values=(id, pid, PLU, name, price, productgroup, pprice, location))
        self.tree.heading("#1", text="Stregkode")
        self.tree.heading("#2", text="PLU")
        self.tree.heading("#3", text="Navn")
        self.tree.heading("#4", text="Pris")
        self.tree.heading("#5", text="Produktgruppe")
        self.tree.heading("#6", text="Indkøbspris")
        self.tree.heading("#7", text="Placering")

    def products(self):
        def close():
            self.productWindow.destroy()
            self.productWindow.update()
        def mangler():
            print('Mangler at blive implementeret')
        def new_product():
            def close():
                self.create_newproduct.destroy()
                self.create_newproduct.update()
            def save_data():#forkert
                self.Data = Data()
                name = str(self.input_name.get())
                pid = str(self.input_pid.get())
                PLU = str(self.input_PLU.get())
                price = float(self.input_price.get())
                pgroup = str(self.input_pgroup.get())
                pprice = float(self.input_pprice.get())
                location = str(self.input_location.get())
                self.Data.new_product(name, pid, PLU, price, pgroup, pprice, location)
                close()
                self.update_product_tabel()

            self.create_newproduct = tk.Toplevel()
            self.create_newproduct.geometry("1080x720")
            self.create_newproduct.grab_set()
            self.create_newproduct.wm_title('Nyt produkt')
            self.save_nprodut = tk.Button(self.create_newproduct, text = 'Gem produkt')
            self.save_nprodut['command'] = save_data
            self.save_nprodut.grid(column=1, sticky="nsew")
            self.back_nprodut = tk.Button(self.create_newproduct, text = 'Tilbage')
            self.back_nprodut['command'] = close
            self.back_nprodut.grid(column=1, sticky="nsew")
            tk.Label(self.create_newproduct, text='Indtast navn: ').grid(row=0, column=2)
            self.input_name = tk.Entry(self.create_newproduct)
            self.input_name.grid(row=1, column=2)
            tk.Label(self.create_newproduct, text='Indtast produkt ID: ').grid(row=2, column=2)
            self.input_pid = tk.Entry(self.create_newproduct)
            self.input_pid.grid(row=3, column=2)
            tk.Label(self.create_newproduct, text='Indtast PLU(eventuelt): ').grid(row=4, column=2)
            self.input_PLU = tk.Entry(self.create_newproduct)
            self.input_PLU.grid(row=5, column=2)
            tk.Label(self.create_newproduct, text='Indtast pris: ').grid(row=6, column=2)
            self.input_price = tk.Entry(self.create_newproduct)
            self.input_price.grid(row=7, column=2)
            tk.Label(self.create_newproduct, text='Indtast produktgruppe: ').grid(row=8, column=2)
            self.input_pgroup = tk.Entry(self.create_newproduct)
            self.input_pgroup.grid(row=9, column=2)
            tk.Label(self.create_newproduct, text='Indtast indkøbspris: ').grid(row=10, column=2)
            self.input_pprice = tk.Entry(self.create_newproduct)
            self.input_pprice.grid(row=11, column=2)
            tk.Label(self.create_newproduct, text='Indtast placering: ').grid(row=12, column=2)
            self.input_location = tk.Entry(self.create_newproduct)
            self.input_location.grid(row=13, column=2)

        def delete_product_():
            def close():
                self.delete_product.destroy()
                self.delete_product.update()

            def get_item():
                item = self.tree.focus()
                dic = self.tree.item(item)
                list = dic.get('values')
                id = list[0]
                navn = list[3]
                return id, navn

            def delete_product():
                self.Data.delete_product(id)
                self.update_product_tabel()
                close()

            self.delete_product = tk.Toplevel()
            self.delete_product.geometry("1080x720")
            self.delete_product.grab_set()
            self.delete_product.wm_title('Slet varer')

            id, item = get_item()

            self.back_nprodutg = tk.Button(self.delete_product, text = 'Tilbage')
            self.back_nprodutg['command'] = close
            self.back_nprodutg.grid(column=1, sticky="nsew")

            self.save_nprodutg = tk.Button(self.delete_product, text = 'Slet vare')
            self.save_nprodutg.grid(column=1, sticky="nsew")
            self.save_nprodutg['command'] = delete_product

            tk.Label(self.delete_product, text='Det valgte produkt er: {}'.format(item)).grid(row=0, column=2)

        def edit_product_():
            def close():
                self.create_newproductgroup.destroy()
                self.create_newproductgroup.update()

            def get_item():
                item = self.tree.focus()
                dic = self.tree.item(item)
                list = dic.get('values')
                id = list[0]
                pid = list[1]
                PLU = list[2]
                name = list[3]
                price = list[4]
                productgroup = list[5]
                pprice = list[6]
                location = list[7]
                return id, name

            def edit_product():
                new_name = self.epgroup_input.get()
                print(type(old_id))
                self.Data.edit_product(old_id, new_name)
                self.update_product_tabel()
                close()

            self.create_newproductgroup = tk.Toplevel()
            self.create_newproductgroup.geometry("1080x720")
            self.create_newproductgroup.grab_set()
            self.create_newproductgroup.wm_title('Ret varer')

            old_id, old_item = get_item()

            self.back_nprodutg = tk.Button(self.create_newproductgroup, text = 'Tilbage')
            self.back_nprodutg['command'] = close
            self.back_nprodutg.grid(column=1, sticky="nsew")

            self.save_nprodutg = tk.Button(self.create_newproductgroup, text = 'Gem varegruppe')
            self.save_nprodutg.grid(column=1, sticky="nsew")
            self.save_nprodutg['command'] = edit_product

            tk.Label(self.create_newproductgroup, text='Den valgte produktgruppe er: {}'.format(old_item)).grid(row=0, column=2)
            tk.Label(self.create_newproductgroup, text='Indtast rettelse: ').grid(row=1, column=2)

            self.epgroup_input = tk.Entry(self.create_newproductgroup)
            self.epgroup_input.grid(row=1, column=3)

        self.productWindow = tk.Toplevel()
        self.productWindow.geometry("1080x720")
        self.productWindow.grab_set()
        self.productWindow.wm_title('Varer')

        self.back = tk.Button(self.productWindow, text = 'Tilbage')
        self.back['command'] = close
        self.back.grid(row=0, column=1, sticky="nsew")

        self.newproduct = tk.Button(self.productWindow, text = 'Ny vare')
        self.newproduct['command'] = new_product
        self.newproduct.grid(row=1, column=1, sticky="nsew")

        self.editproduct = tk.Button(self.productWindow, text = 'Ret vare')
        self.editproduct['command'] = edit_product_
        self.editproduct.grid(row=2, column=1, sticky="nsew")

        self.deleteproduct = tk.Button(self.productWindow, text = 'Slet vare')
        self.deleteproduct['command'] = delete_product_
        self.deleteproduct.grid(row=3, column=1, sticky="nsew")


        self.tree = ttk.Treeview(self.productWindow, columns=("Id", "Produkt id", "PLU", "Name", "Pris", "Produktgruppe", "Indkøbspris", "Placering"), show = 'headings')
        self.tree.heading("#1", text="Varer")
        self.tree['displaycolumns'] = ("Produkt id", "PLU", "Name", "Pris", "Produktgruppe", "Indkøbspris", "Placering")
        self.tree.bind('<ButtonRelease-1>', self.select_item)
        self.update_product_tabel()
        self.tree.grid(row=0, rowspan=4, column = 2)

if __name__ == "__main__":
    root = tk.Tk()
    Main(root).pack(fill="both", expand=True)
    root.title('Growingstore program')
    root.geometry("1080x720")
    root.mainloop()
