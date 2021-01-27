import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
import numpy as np
from logiklag import *
from datalag import Data
print("Import complete")

dic = ""

class Main(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)

        self.Data = Data()
        # self.Product = Product()

        self.logo = tk.Label(self, text="Logo")
        self.buttons = []
        for i in range(6):
            self.buttons.append(tk.Button(self))
        self.main = tk.Frame(self)

        self.logo.grid(row=0, column=0, rowspan=2, sticky="nsew")
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
        self.main.grid(row=2, column=2, columnspan=2, rowspan=6)

        for row in range(8):
            self.grid_rowconfigure(row, weight=1)
        for col in range(3):
            self.grid_columnconfigure(col, weight=1)

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
    def products(self):
        def close():
            self.productWindow.destroy()
            self.productWindow.update()
        def mangler():
            pass

        self.productWindow = tk.Toplevel()
        self.productWindow.geometry("1080x720")
        self.productWindow.grab_set()
        self.productWindow.wm_title('Varer')

        self.back = tk.Button(self.productWindow, text = 'Tilbage')
        self.back['command'] = close
        self.back.grid(row=0, column=1, sticky="nsew")

        self.newproduct = tk.Button(self.productWindow, text = 'Ny vare')
        self.newproduct['command'] = mangler
        self.newproduct.grid(row=1, column=1, sticky="nsew")

        self.editproduct = tk.Button(self.productWindow, text = 'Ret vare')
        self.editproduct['command'] = mangler
        self.editproduct.grid(row=2, column=1, sticky="nsew")

        self.deleteproduct = tk.Button(self.productWindow, text = 'Slet vare')
        self.deleteproduct['command'] = mangler
        self.deleteproduct.grid(row=3, column=1, sticky="nsew")


        self.tree = ttk.Treeview(self.productWindow, columns=("Id", "Name"), show = 'headings')
        self.tree.heading("#1", text="Varer")
        self.tree['displaycolumns'] = ('Name')
        self.tree.bind('<ButtonRelease-1>', self.select_item)
        self.update_productgroup_tabel()
        self.tree.grid(row=0, rowspan=4, column = 2)

if __name__ == "__main__":
    root = tk.Tk()
    Main(root).pack(fill="both", expand=True)
    root.geometry("1080x720")
    root.mainloop()
