# import tkinter and rename to 'tk' for easier use
import threading
import time
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
from tkinter import font


class TemplateGUI(tk.Tk):

    def __init__(self, parent):
        tk.Tk.__init__(self, parent)
        self.parent = parent
        self.input_path = tk.StringVar()
        self.input_path.set('<Input folder path>')
        self.second_path = tk.StringVar()
        self.second_path.set('<Input folder path>')
        self.style = ttk.Style()
        self.style_main_window()
        self.create_widgets()
        self.style_widgets()

    def style_main_window(self):
        self.title('Template GUI title')
        # self.geometry('515x200')
        self.resizable(width=False, height=False)
        self.focus_force()

    def style_widgets(self):
        theme_colors = {'Primary': '#D3DADB', 'Second': '#525251', 'Third': '#3B627E',
                        'Fourth': '#5799C3', 'Fifth': '#8DCFDA', 'Sixth': '#B7F0ED'}

        self.style.map('TEntry',
                             background=('active',theme_colors['Primary']))
        self.style.configure('TButton',
                             foreground=theme_colors['Third'],
                             background=theme_colors['Primary'],
                             padding=5)
        self.style.configure('Horizontal.TProgressbar', padding=10)

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

        self.frame_C = ttk.Frame(self)
        self.frame_C.grid(column=0, row=5)

        self.button_run = ttk.Button(self.frame_C, text='Run',
                                     command=self.on_button_click_run)
        self.button_run.grid(column=0, row=0)

        self.frame_D = ttk.Frame(self)
        self.frame_D.grid(column=0, row=6)

        self.progress_bar = ttk.Progressbar(self.frame_D, orient='horizontal',
                                            mode='indeterminate', length=300)
        self.progress_bar.grid(column=0, row=0)

    def on_button_click_input(self):
        input_file_location = filedialog.askopenfilename()
        self.input_path.set(input_file_location)

    def on_button_click_second(self):
        second_file_location = filedialog.askopenfilename()
        self.second_path.set(second_file_location)

    def on_button_click_run(self):
        self.button_run.configure(state='disable')
        self.start_thread()

    def undefined_process(self):
        time.sleep(10)
        print('done')
        self.progress_bar.stop()
        self.button_run.configure(state='enable')

    def start_thread(self):
        self.thread_one = threading.Thread(target=self.undefined_process)
        self.progress_bar.start()
        self.thread_one.start()


# Execute a 'main' when the program is run
if __name__ == '__main__':
    app = TemplateGUI(None)
    app.mainloop()
