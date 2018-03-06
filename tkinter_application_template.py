import tkinter as tk
from tkinter import ttk


class MainApplication(tk.Tk):

    def __init__(self, parent, *args, **kwargs):
        tk.Tk.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.title('tkinter application v1.0')
        self.resizable(width=False, height=False)
        self.focus_force()

        self.input_variable = tk.StringVar()
        self.second_variable = tk.StringVar()
        self.main_frame = ttk.Frame(self)

        self.create_main_widgets(self.main_frame)

    def create_main_widgets(self, frame):

        frame.grid(column=0, row=0, sticky='nsew')

        main_label = ttk.Label(frame, text='Main Label')
        main_label.grid(column=0, row=0, sticky='nsew', padx=4, pady=4)

        self.file_entry_frame(frame, self.input_variable, 'Input Frame')
        self.file_entry_frame(frame, self.second_variable, 'Second Input Frame')


    def file_entry_frame(self, parent_frame, tk_string_variable, frame_label):

        input_frame = ttk.Labelframe(parent_frame, text=frame_label)
        input_frame.grid(column=0, row=0, sticky='nsew')

        input_field = ttk.Entry(input_frame, textvariable=tk_string_variable)
        input_field.grid(column=0, row=1, sticky='nsew', padx=6, pady=6)




if __name__ == '__main__':
    app = MainApplication(None)
    app.mainloop()
