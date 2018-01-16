import tkinter as tk


class GUI:
    def __init__(self, master):
        self.master = master
        master.title('A simple GUI')

        self.label = tk.Label(master, text='This is our first GUI!')
        self.label.pack()


root = tk.Tk()
my_gui = GUI(root)
root.mainloop()
