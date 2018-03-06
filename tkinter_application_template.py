import tkinter as tk
from tkinter import ttk


class MainApplication(tk.Tk):

    def __init__(self, parent):
        tk.Tk.__init__(self, parent)
        self.parent = parent


if __name__ == '__main__':
    app = MainApplication(None)
    app.mainloop()
