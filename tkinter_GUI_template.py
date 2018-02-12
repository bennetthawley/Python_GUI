# import tkinter and rename to 'tk' for easier use
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog


class TemplateGUI(tk.Tk):

    def __init__(self, parent):
        tk.Tk.__init__(self, parent)
        self.parent = parent
        self.title('Template GUI title')
        self.input_path = tk.StringVar()
        self.input_path.set('<Input folder path>')
        self.second_path = tk.StringVar()
        self.second_path.set('<Input folder path>')
        self.create_widgets()
        self.style_widgets()

    def style_widgets(self):
        self.style = ttk.Style()
        self.style.configure('TEntry', foreground='green', background='black')
        self.style.configure('TButton', foreground='red', padding = 4)

    def create_widgets(self):
        self.grid()

        self.style = ttk.Style()
        self.style.configure('TEntry', width=50)

        self.label = ttk.Label(self, text='Template tkinter GUI')
        self.label.grid(column=0, row=0)

        self.frame_A = ttk.Labelframe(self, text='Input Frame')
        self.frame_A.grid(column=0, row=1)

        self.entry_A1 = ttk.Entry(self.frame_A, textvariable=self.input_path)
        self.entry_A1.grid(column=0, row=0)

        self.button_A1 = ttk.Button(self.frame_A, text='browse',
                                    command=self.on_button_click)
        self.button_A1.grid(column=1, row=0)

        self.frame_B = ttk.Labelframe(self, text='Secondary Frame')
        self.frame_B.grid(column=0, row=2)

        self.entry_B1 = ttk.Entry(self.frame_B, textvariable=self.second_path)
        self.entry_B1.grid(column=0, row=0)

        self.button_B1 = ttk.Button(self.frame_B, text='browse',
                                    command=self.on_button_click)
        self.button_B1.grid(column=1, row=0)

        self.seperation = ttk.Separator(self)
        self.seperation.grid(column=0, row=3)

        self.button_run = ttk.Button(self, text='Run',
                                    command=self.on_button_click)
        self.button_run.grid(column=0, row=4)

    def on_button_click(self):
        self.file_location = filedialog.askopenfilename()
        print(self.file_location)


# Execute a 'main' when the program is run
if __name__ == '__main__':
    app = TemplateGUI(None)
    app.mainloop()
