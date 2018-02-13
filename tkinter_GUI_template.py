# import tkinter and rename to 'tk' for easier use
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog


class TemplateGUI(tk.Tk):

    def __init__(self, parent):
        tk.Tk.__init__(self, parent)
        self.parent = parent
        self.input_path = tk.StringVar()
        self.input_path.set(r'/Users/Bennett/Documents/GitHub/Automate_the_boring_stuff')
        self.second_path = tk.StringVar()
        self.second_path.set('<Input folder path>')
        self.style_main_window()
        self.create_widgets()
        self.style_widgets()

    def style_main_window(self):
        self.title('Template GUI title')
        #self.geometry('515x200')
        self.resizable(width=False, height=False)
        self.focus_force()

    def style_widgets(self):
        self.style = ttk.Style()
        self.style.configure('TEntry', foreground='purple')
        self.style.configure('TButton', foreground='red', padding=4)

        # for element in self.winfo_children():
        #     element.grid_configure(padx=4, pady=4)


    def create_widgets(self):
        self.label = ttk.Label(self, text='Template tkinter GUI')
        self.label.grid(column=0, row=0)

        self.frame_A = ttk.Labelframe(self, text='Input Frame')
        self.frame_A.grid(column=0, row=1)

        self.entry_A1 = ttk.Entry(self.frame_A, textvariable=self.input_path,
                                  width=50)
        self.entry_A1.grid(column=0, row=0)

        self.button_A1 = ttk.Button(self.frame_A, text='Browse',
                                    command=self.on_button_click_input)
        self.button_A1.grid(column=1, row=0)

        self.frame_B = ttk.Labelframe(self, text='Secondary Frame')
        self.frame_B.grid(column=0, row=2)

        self.entry_B1 = ttk.Entry(self.frame_B, textvariable=self.second_path,
                                  width=50)
        self.entry_B1.grid(column=0, row=0)

        self.button_B1 = ttk.Button(self.frame_B, text='Browse',
                                    command=self.on_button_click_second)
        self.button_B1.grid(column=1, row=0)

        self.frame_C = ttk.Labelframe(self)
        self.frame_C.grid(column=0, row=5)

        self.button_run = ttk.Button(self.frame_C, text='Run',
                                     command=self.on_button_click_run)
        self.button_run.grid(column=0, row=0)

    def on_button_click_input(self):
        self.input_file_location = filedialog.askopenfilename()
        self.input_path.set(self.input_file_location)

    def on_button_click_second(self):
        self.second_file_location = filedialog.askopenfilename()
        self.second_path.set(self.second_file_location)

    def on_button_click_run(self):
        self.update_idletasks()

        self.label_result = ttk.Label(self.frame_C, text=self.entry_A1.get())
        self.label_result.grid(column=0, row=1)
        self.label_result2 = ttk.Label(self.frame_C, text=self.entry_B1.get())
        self.label_result2.grid(column=0, row=2)



# Execute a 'main' when the program is run
if __name__ == '__main__':
    app = TemplateGUI(None)
    app.mainloop()
