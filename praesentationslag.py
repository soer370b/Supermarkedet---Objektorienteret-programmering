class Main(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)

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
        self.varer['command'] = self.vare
        self.log_ud = self.buttons[5]
        self.varer['text'] = 'Log ud'
        self.varer['command'] = self.vare
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
        self.productgroupWindow = tk.Toplevel(self)
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

    def createnewproductgroup(self):
        self.create_newproductgroup = tk.Toplevel()
        self.create_newproductgroup.grab_set()
        self.create_newproductgroup.wm_title('Ny produktgruppe')

        self.back = tk.Button(self.create_newproductgroup, text = 'Ny produktgruppe')
        self.back.grid(column=1, sticky="nsew")



if __name__ == "__main__":
    root = tk.Tk()
    Main(root).pack(fill="both", expand=True)
    root.geometry("1080x720")
    root.mainloop()
