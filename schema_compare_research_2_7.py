import Tkinter as tk
import threading
import time
import ttk
import tkMessageBox
import tkFileDialog
import tkFont
import Queue
import os.path
import zipfile



class MainApplication(tk.Tk):

    def __init__(self, parent, *args, **kwargs):
        tk.Tk.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.queue = Queue.Queue()
        self.input_variable = tk.StringVar()
        self.input_variable.set(r'C:/Users/Bennett/Documents/Python Scripts/DNCH.zip')
        self.second_variable = tk.StringVar()
        self.second_variable.set(r'C:\Users\Bennett\Documents\Python Scripts\Geodatabases.zip')
        self.output_variable = tk.StringVar()
        self.output_variable.set(r'C:\Users\Bennett\Documents\Python Scripts')
        self.radio_variable = tk.StringVar()
        self.combobox_variable = tk.StringVar()
        self.combobox_variable.set('<Select DNC Scale>')
        self.configure_main_gui()
        self.create_main_widgets()
        self.style_widgets()

    def configure_main_gui(self):
        self.title('schema research v1.0')
        self.resizable(width=False, height=False)
        self.focus_force()

    def style_widgets(self):
        theme_colors = {'light_blue': '#c0e0de',
                        'dark_blue': '#0d324d',
                        'dark_grey': '#2b303a',
                        'almost_black': '#100007',
                        'coral': '#ff220c'}
        style = ttk.Style(self)
        style.theme_use('clam')
        tkFont.families(self)
        font = 'default 16 bold'
        style.configure('.', font=font,
                        foreground=theme_colors['light_blue'],
                        background=theme_colors['dark_blue'],
                        fieldbackground=theme_colors['almost_black'],
                        bordercolor=theme_colors['light_blue'],
                        lightcolor=theme_colors['light_blue'],
                        darkcolor=theme_colors['light_blue'],
                        troughcolor=theme_colors['almost_black'],
                        relief=theme_colors['coral'])

        style.map('TButton',
                  foreground=[('active', theme_colors['dark_blue']),
                              ('pressed', theme_colors['coral']),
                              ('disabled', theme_colors['dark_grey'])],
                  background=[('active', theme_colors['coral']),
                              ('pressed', theme_colors['coral']),
                              ('disabled', theme_colors['almost_black'])],
                  highlightcolor=[('active', theme_colors['coral']),
                                  ('pressed', theme_colors['coral']),
                                  ('disabled', theme_colors['almost_black'])],
                  bordercolor=[('active', theme_colors['coral']),
                               ('pressed', theme_colors['coral']),
                               ('disabled', theme_colors['dark_grey'])],
                  troughcolor=[('active', theme_colors['coral']),
                               ('pressed', theme_colors['coral']),
                               ('disabled', theme_colors['dark_grey'])],
                  lightcolor=[('active', theme_colors['coral']),
                              ('pressed', theme_colors['coral']),
                              ('disabled', theme_colors['dark_grey'])],
                  darkcolor=[('active', theme_colors['coral']),
                             ('pressed', theme_colors['coral']),
                             ('disabled', theme_colors['dark_grey'])])
        style.map('TCheckbutton',
                  foreground=[('active', theme_colors['coral']),
                              ('pressed', theme_colors['coral']),
                              ('disabled', theme_colors['dark_grey'])],
                  background=[('active', theme_colors['dark_blue']),
                              ('pressed', theme_colors['coral']),
                              ('disabled', theme_colors['almost_black'])],
                  indicatorcolor=[('selected', theme_colors['coral']),
                                  ('pressed', theme_colors['coral']),
                                  ('disabled', theme_colors['almost_black'])])

        style.map('TCombobox',
                  foreground=[('active', theme_colors['coral']),
                              ('focus', theme_colors['coral']),
                              ('!focus', theme_colors['light_blue']),
                              ('readonly', theme_colors['coral']),
                              ('disabled', theme_colors['dark_grey'])],
                  background=[('active', theme_colors['coral']),
                              ('focus', theme_colors['coral']),
                              ('!focus', theme_colors['light_blue']),
                              ('readonly', theme_colors['dark_blue']),
                              ('disabled', theme_colors['almost_black'])],
                  fieldbackground=[('active', theme_colors['almost_black']),
                                   ('focus', theme_colors['almost_black']),
                                   ('!focus', theme_colors['almost_black']),
                                   ('readonly', theme_colors['dark_grey']),
                                   ('disabled', theme_colors['dark_grey'])],
                  highlightcolor=[('active', theme_colors['coral']),
                                  ('focus', theme_colors['coral']),
                                  ('!focus', theme_colors['coral']),
                                  ('readonly', theme_colors['almost_black']),
                                  ('disabled', theme_colors['almost_black'])],
                  indicatorcolor=[('selected', theme_colors['coral']),
                                  ('pressed', theme_colors['coral']),
                                  ('focus', theme_colors['coral']),
                                  ('!focus', theme_colors['coral']),
                                  ('disabled', theme_colors['almost_black'])],
                  bordercolor=[('active', theme_colors['coral']),
                               ('focus', theme_colors['coral']),
                               ('!focus', theme_colors['light_blue']),
                               ('readonly', theme_colors['almost_black']),
                               ('disabled', theme_colors['almost_black'])],
                  troughcolor=[('active', theme_colors['coral']),
                               ('focus', theme_colors['coral']),
                               ('!focus', theme_colors['light_blue']),
                               ('readonly', theme_colors['almost_black']),
                               ('disabled', theme_colors['almost_black'])],
                  lightcolor=[('active', theme_colors['coral']),
                              ('focus', theme_colors['coral']),
                              ('!focus', theme_colors['light_blue']),
                              ('readonly', theme_colors['almost_black']),
                              ('disabled', theme_colors['almost_black'])],
                  darkcolor=[('active', theme_colors['coral']),
                             ('focus', theme_colors['coral']),
                             ('!focus', theme_colors['light_blue']),
                             ('readonly', theme_colors['almost_black']),
                             ('disabled', theme_colors['almost_black'])])

        style.map('TEntry',
                  foreground=[('focus', theme_colors['coral']),
                              ('!focus', theme_colors['light_blue']),
                              ('readonly', theme_colors['light_blue']),
                              ('disabled', theme_colors['dark_grey'])],
                  fieldbackground=[('focus', theme_colors['almost_black']),
                                   ('!focus', theme_colors['almost_black']),
                                   ('readonly', theme_colors['dark_grey']),
                                   ('disabled', theme_colors['dark_grey'])],
                  highlightcolor=[('active', theme_colors['coral']),
                                  ('focus', theme_colors['coral']),
                                  ('!focus', theme_colors['coral']),
                                  ('disabled', theme_colors['almost_black'])],
                  indicatorcolor=[('selected', theme_colors['coral']),
                                  ('pressed', theme_colors['coral']),
                                  ('focus', theme_colors['coral']),
                                  ('disabled', theme_colors['almost_black'])],
                  bordercolor=[('active', theme_colors['coral']),
                               ('focus', theme_colors['coral']),
                               ('!focus', theme_colors['light_blue']),
                               ('disabled', theme_colors['almost_black'])],
                  troughcolor=[('active', theme_colors['coral']),
                               ('focus', theme_colors['coral']),
                               ('!focus', theme_colors['light_blue']),
                               ('disabled', theme_colors['almost_black'])],
                  lightcolor=[('active', theme_colors['coral']),
                              ('focus', theme_colors['coral']),
                              ('!focus', theme_colors['light_blue']),
                              ('disabled', theme_colors['almost_black'])],
                  darkcolor=[('active', theme_colors['coral']),
                             ('focus', theme_colors['coral']),
                             ('!focus', theme_colors['light_blue']),
                             ('disabled', theme_colors['almost_black'])])
        style.map('TRadiobutton',
                  foreground=[('active', theme_colors['coral']),
                              ('pressed', theme_colors['coral']),
                              ('focus', theme_colors['coral']),
                              ('disabled', theme_colors['dark_grey'])],
                  background=[('active', theme_colors['dark_blue']),
                              ('pressed', theme_colors['coral']),
                              ('disabled', theme_colors['almost_black'])],
                  indicatorcolor=[('selected', theme_colors['coral']),
                                  ('pressed', theme_colors['coral']),
                                  ('focus', theme_colors['coral']),
                                  ('disabled', theme_colors['almost_black'])],
                  highlightcolor=[('active', theme_colors['coral']),
                                  ('focus', theme_colors['coral']),
                                  ('pressed', theme_colors['coral']),
                                  ('disabled', theme_colors['almost_black'])])
        style.configure('Horizontal.TProgressbar',
                        foreground=theme_colors['coral'],
                        background=theme_colors['coral'],
                        bordercolor=theme_colors['almost_black'],
                        troughcolor=theme_colors['almost_black'],
                        lightcolor=theme_colors['coral'],
                        darkcolor=theme_colors['coral'])

    def create_main_widgets(self):
        try:
            entry_fonts = 'default 16 bold'

            main_frame = ttk.Frame(self)
            main_frame.grid(column=0, row=0, sticky='news')
            main_frame.columnconfigure(0, weight=1)

            main_label = ttk.Label(main_frame, text='Schema Compare')
            main_label.grid(column=0, row=0, sticky='ew', padx=4, pady=4)
            main_label.columnconfigure(0, weight=1)

            input_frame = ttk.Labelframe(main_frame, text='Base "Gold" Schema')
            input_frame.grid(column=0, row=1, sticky='news', padx=4, pady=4)

            combobox_1 = ttk.Combobox(input_frame,
                                      values=['Harbor - DNCH',
                                              'Approach - DNCA',
                                              'Coastal - DNCC',
                                              'General - DNCG'],
                                      textvariable=self.combobox_variable,
                                      state='readonly',
                                      font=entry_fonts)
            combobox_1.grid(column=0, row=0, columnspan=2, padx=2, pady=2)

            input_entry = ttk.Entry(input_frame, textvariable=self.input_variable,
                                    width=75, font=entry_fonts)
            input_entry.grid(column=0, row=1, sticky='ew', padx=4, pady=4)

            input_button = ttk.Button(input_frame, text='Browse',
                                      command=self.get_input_filepath)
            input_button.grid(column=1, row=1, sticky='ew', padx=4, pady=4)

            second_frame = ttk.Labelframe(main_frame, text='Test Schema')
            second_frame.grid(column=0, row=2, sticky='ew', padx=4, pady=4)

            radio_button_1 = ttk.Radiobutton(second_frame, text='Geodatabase - .gdb',
                                             value='Geodatabase - .gdb',
                                             variable=self.radio_variable)
            radio_button_1.grid(column=0, row=0, sticky='ew', padx=2, pady=2)

            radio_button_2 = ttk.Radiobutton(second_frame, text='Zipfile - .zip',
                                             value='Zipfile - .zip',
                                             variable=self.radio_variable)
            radio_button_2.grid(column=0, row=1, sticky='ew', padx=2, pady=2)

            second_entry = ttk.Entry(second_frame, textvariable=self.second_variable,
                                     width=75, font=entry_fonts)
            second_entry.grid(column=0, row=2, sticky='ew', padx=4, pady=4)

            second_button = ttk.Button(second_frame, text='Browse',
                                       command=self.get_second_filepath)
            second_button.grid(column=1, row=2, sticky='ew', padx=4, pady=4)

            output_frame = ttk.Labelframe(main_frame, text='Output Frame')
            output_frame.grid(column=0, row=3, sticky='ew', padx=4, pady=4)

            output_entry = ttk.Entry(output_frame, textvariable=self.output_variable,
                                     width=75, font=entry_fonts)
            output_entry.grid(column=0, row=0, sticky='ew', padx=4, pady=4)

            output_button = ttk.Button(output_frame, text='Browse',
                                       command=self.get_output_filepath)
            output_button.grid(column=1, row=0, sticky='ew', padx=4, pady=4)

            processing_frame = ttk.Labelframe(main_frame, text='Processing Frame')
            processing_frame.grid(column=0, row=4, padx=4, pady=4)

            self.run_button = ttk.Button(processing_frame, text='Run',
                                         command=self.run_application)
            self.run_button.grid(column=0, row=0, padx=4, pady=4)

            self.status_bar = ttk.Progressbar(processing_frame, mode='determinate',
                                              length=300)
            self.status_bar.grid(column=0, row=1, padx=4, pady=4)

            self.messages_text = tk.Text(processing_frame, wrap=tk.WORD, height=15, width=100)
            self.messages_text.configure(state='disabled', background='#100007',
                                         foreground='#c0e0de', font='default 12 bold')
            self.messages_text.grid(column=0, row=2, padx=4, pady=4, sticky='news')

        except Exception as e:
            tkMessageBox.showerror('Error', e)

    def get_input_filepath(self):
        input_filepath = tkFileDialog.askopenfilename(title='Select Input File')
        self.input_variable.set(input_filepath)

    def get_second_filepath(self):
        if self.radio_variable.get() == 'Geodatabase - .gdb':
            input_filepath = tkFileDialog.askdirectory(title='Select Input .gdb')
            self.second_variable.set(input_filepath)
        elif self.radio_variable.get() == 'Zipfile - .zip':
            input_filepath = tkFileDialog.askopenfilename(title='Select Input .zip')
            self.second_variable.set(input_filepath)
        else:
            tkMessageBox.showwarning('Check file inputs', 'Please check the input files')

    def get_output_filepath(self):
        output_filepath = tkFileDialog.askdirectory(title='Select Output Directory')
        self.output_variable.set(output_filepath)

    def check_filepaths(self):
        filepaths = [self.input_variable.get(), self.second_variable.get(),
                     self.output_variable.get()]
        for path in filepaths:
            if os.path.exists(path):
                pass
            else:
                return False

        return True

    def write_to_messages(self, message):
        try:
            self.messages_text.configure(state='normal')
            self.messages_text.insert('end', message)
            self.messages_text.configure(state='disabled')
        except Exception as e:
            self.status_bar.stop()
            return e

    def clear_messages(self):
        try:
            self.messages_text.configure(state='normal')
            self.messages_text.delete('1.0', tk.END)
            self.messages_text.configure(state='disabled')
        except Exception as e:
            self.status_bar.stop()
            return e

    def write_start_message(self):
        try:
            self.messages_text.configure(state='normal')
            self.messages_text.insert('end', '{}Run: {}{}\n'.format(
                ('=' * 5), time.strftime("%c"), ('=' * 5)))

            self.messages_text.insert('end', 'Input: {}\n\n'.format(
                self.input_variable.get()))

            self.messages_text.insert('end', 'Processing with: {}\n\n'.format(
                self.second_variable.get()))

            self.messages_text.insert('end', 'Output: {}\n\n'.format(
                self.output_variable.get()))

            self.messages_text.configure(state='disabled')
        except Exception as e:
            self.status_bar.stop()
            return e

    def run_application(self):
        try:
            if self.check_filepaths():
                self.run_button.configure(state='disabled')
                self.clear_messages()
                self.write_start_message()
                self.thread = ThreadedClient(self.queue,
                                             self.input_variable.get(),
                                             self.second_variable.get(),
                                             self.output_variable.get())
                self.thread.start()
                self.periodiccall()
            else:
                tkMessageBox.showwarning('Enter filepaths', 'Please check all filepaths')
        except Exception as e:
            return e
            tkMessageBox.showerror('Error', e)

    def periodiccall(self):
        self.checkqueue()
        self.status_bar.start()
        if self.thread.is_alive():
            self.after(100, self.periodiccall)
        else:
            self.run_button.configure(state="active")
            self.status_bar.stop()
            self.write_to_messages('\nProcessing complete!')

    def checkqueue(self):
        while self.queue.qsize():
            try:
                msg = self.queue.get(0)
                self.write_to_messages(msg)
            except Queue.Empty:
                pass


class ThreadedClient(threading.Thread):

    def __init__(self, queue, base, test, output):
        threading.Thread.__init__(self)
        self.queue = queue
        self.base = base
        self.test = test
        self.output = output

    def run(self):
        self.queue.put('Starting Schema Comparison...\n\n')
        self.unzip_files(self.base)
        self.unzip_files(self.test)

    def unzip_files(self, zip_file):
        unzip_location = os.path.join(self.output,'extracted_zip_schemas')
        self.queue.put('Extracting {}\nto: {}\n\n'.format(zip_file, unzip_location))
        with zipfile.ZipFile(zip_file, 'r') as zfile:
            namelist = zfile.namelist()
            unique_gdbs = set([os.path.split(gdb)[0] for gdb in namelist])
            if len(unique_gdbs) == 1:
                zfile.extractall(unzip_location)
            elif len(unique_gdbs) > 1:
                selected_gdb = list(unique_gdbs)[0] # change to selection from GUI list
                extract = [item for item in namelist if item.startswith(selected_gdb)]
                zfile.extractall(unzip_location, extract)
            else:
                self.queue.put('There are no geodatabases in this .zip')







if __name__ == '__main__':
    app = MainApplication(None)
    app.mainloop()
