# import tkinter and rename to 'tk' for easier use
import tkinter as tk
from tkinter import ttk


class TemplateGUI(tk.Tk):

    def __init__(self, parent):
        tk.Tk.__init__(self, parent)
        self.parent = parent
        self.title('Template GUI title')
        self.create_widgets()

    def create_widgets(self):
        self.grid()

        self.label = ttk.Label(self, text='Template tkinter GUI')
        self.label.grid(column=0, row=0)

        self.frame_A = ttk.Labelframe(self, text='Input Frame')
        self.frame_A.grid(column=0, row=1)

        self.entry_A1 = ttk.Entry(self.frame_A)
        self.entry_A1.grid(column=0, row=0)

        self.button_A1 = ttk.Button(self.frame_A, text='browse',
                                    command=self.on_button_click)
        self.button_A1.grid(column=1, row=0)

    def on_button_click(self):
        print('hello')


# Execute a 'main' when the program is run
if __name__ == '__main__':
    app = TemplateGUI(None)
    app.mainloop()
