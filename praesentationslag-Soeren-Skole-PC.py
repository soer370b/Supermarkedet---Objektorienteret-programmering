import tkinter as tk


#variable
#knap størrelse
height = 8
width = 20

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.geometry('1080x720')
        self.pack(fill = 'both', expand = True)
        self.create_widgets()

    def create_widgets(self):
        self.varegruppe = tk.Button(self)
        self.varegruppe["text"] = "Varegrupper"
        self.varegruppe["command"] = self.varegruupper
        self.varegruppe['height'] = height
        self.varegruppe['width'] = width
        self.varegruppe.pack(side='top')

        self.vare = tk.Button(self)
        self.vare["text"] = "Vare"
        self.vare["command"] = self.varer
        self.vare['height'] = height
        self.vare['width'] = width
        self.vare.pack(side='top')

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit['height'] = height
        self.quit['width'] = width
        self.quit.pack(side='top')

    def varegruupper(self):
        print("Varegrupper!")

    def varer(self):
        print('Varer')
root = tk.Tk()
app = Application(master=root)
app.mainloop()
