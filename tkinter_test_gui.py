import tkinter as tk
from tkinter import ttk


class GUI:
    def __init__(self, master):
        self.master = master
        self.master.minsize(400,400)
        self.master.title('A simple GUI')

        self.style = ttk.Style()
        self.style.configure('TLabel', padding=4, foreground='blue')
        self.style.configure('TButton', padding=6, foreground='green')

        self.label = ttk.Label(master, text='Label', style='TLabel')
        self.label.grid(row=1, column=1)

        self.separator = ttk.Separator(master, orient='horizontal')
        self.separator.grid(row=2, column=1)

        self.label_2 = ttk.Label(master, text='Label_2', style='TLabel')
        self.label_2.grid(row=3, column=1)

        self.entry = ttk.Entry(master)
        self.entry.grid(row=4, column=1)

        self.button = ttk.Button(master, text="Go!", style='TButton')
        self.button.grid(row=4, column=2)



root = tk.Tk()
my_gui = GUI(root)
root.mainloop()
