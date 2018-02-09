import tkinter as tk
from tkinter import ttk

class SimpleApp(tk.Tk):
    def __init__(self, parent):
        tk.Tk.__init__(self, parent)
        self.parent = parent
        self.initialize()

    def initialize(self):
        pass

if __name__ == '__main__':
    app = SimpleApp(None)
    app.title('My Application')