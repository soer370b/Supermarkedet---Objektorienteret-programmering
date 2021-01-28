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
        self.varer['command'] = self.vare
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

        for row in range(8):
            self.grid_rowconfigure(row, weight=1)
        for col in range(3):
            self.grid_columnconfigure(col, weight=1)

    def varegrup(self):
        print('Varegruppeside')
        self.productgroup_Window()

    def vare(self):
        print('Varer')

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
        self.back.grid(column=1, sticky="nsew")

        self.newproductgroup = tk.Button(self.productgroupWindow, text = 'Ny varegruppe')
        self.newproductgroup['command'] = self.createnewproductgroup
        self.newproductgroup.grid(column=1, sticky="nsew")

        self.editproductgroup = tk.Button(self.productgroupWindow, text = 'Ret varegruppe')
        self.editproductgroup.grid(column=1, sticky="nsew")

        self.deleteproductgroup = tk.Button(self.productgroupWindow, text = 'Slet varegruppe')
        self.deleteproductgroup.grid(column=1, sticky="nsew")

        self.tree = ttk.Treeview(self.productgroupWindow, columns=("Name", "ID"), show = 'headings')
        self.tree.heading("#1", text="Produktgruppe")
        self.tree['displaycolumns'] = ('Name')
        self.tree.grid(column = 2)


    def createnewproductgroup(self):
        def close():
            self.create_newproductgroup.destroy()
            self.create_newproductgroup.update()
        self.create_newproductgroup = tk.Toplevel()
        self.create_newproductgroup.geometry("1080x720")
        self.create_newproductgroup.grab_set()
        self.create_newproductgroup.wm_title('Ny produktgruppe')
        self.back_nprodutg = tk.Button(self.create_newproductgroup, text = 'Tilbage')
        self.back_nprodutg['command'] = close
        self.back_nprodutg.grid(column=1, sticky="nsew")



if __name__ == "__main__":
    root = tk.Tk()
    Main(root).pack(fill="both", expand=True)
    root.title('Growingstore program')
    root.geometry("1080x720")
    root.mainloop()
