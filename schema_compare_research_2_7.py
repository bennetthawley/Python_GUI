import Tkinter as tk
import threading
import time
import ttk
import tkMessageBox
import tkFileDialog
import tkFont
import Queue
import ScrolledText


class MainApplication(tk.Tk):

    def __init__(self, parent, *args, **kwargs):
        tk.Tk.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.queue = Queue.Queue()
        self.input_variable = tk.StringVar()
        #self.input_variable.set(' <Select a file> ')
        self.second_variable = tk.StringVar()
        #self.second_variable.set(' <Select a folder> ')
        self.radio_variable = tk.StringVar()
        # self.checkbox_variable_1 = tk.StringVar()
        # self.checkbox_variable_2 = tk.StringVar()
        # self.checkbox_variable_3 = tk.StringVar()
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
        self.theme_colors = {'light_blue': '#c0e0de',
                        'dark_blue': '#0d324d',
                        'dark_grey': '#2b303a',
                        'almost_black': '#100007',
                        'coral': '#ff220c'}
        style = ttk.Style(self)
        style.theme_use('clam')
        tkFont.families(self)
        font = 'default 16 bold'
        style.configure('.', font=font,
                        foreground=self.theme_colors['light_blue'],
                        background=self.theme_colors['dark_blue'],
                        fieldbackground=self.theme_colors['almost_black'],
                        bordercolor=self.theme_colors['light_blue'],
                        lightcolor=self.theme_colors['light_blue'],
                        darkcolor=self.theme_colors['light_blue'],
                        troughcolor=self.theme_colors['almost_black'],
                        relief=self.theme_colors['coral'])

        style.map('TButton',
                  foreground=[('active', self.theme_colors['dark_blue']),
                              ('pressed', self.theme_colors['coral']),
                              ('disabled', self.theme_colors['dark_grey'])],
                  background=[('active', self.theme_colors['coral']),
                              ('pressed', self.theme_colors['coral']),
                              ('disabled', self.theme_colors['almost_black'])],
                  highlightcolor=[('active', self.theme_colors['coral']),
                                  ('pressed', self.theme_colors['coral']),
                                  ('disabled', self.theme_colors['almost_black'])],
                  bordercolor=[('active', self.theme_colors['coral']),
                               ('pressed', self.theme_colors['coral']),
                               ('disabled', self.theme_colors['dark_grey'])],
                  troughcolor=[('active', self.theme_colors['coral']),
                               ('pressed', self.theme_colors['coral']),
                               ('disabled', self.theme_colors['dark_grey'])],
                  lightcolor=[('active', self.theme_colors['coral']),
                              ('pressed', self.theme_colors['coral']),
                              ('disabled', self.theme_colors['dark_grey'])],
                  darkcolor=[('active', self.theme_colors['coral']),
                             ('pressed', self.theme_colors['coral']),
                             ('disabled', self.theme_colors['dark_grey'])])
        style.map('TCheckbutton',
                  foreground=[('active', self.theme_colors['coral']),
                              ('pressed', self.theme_colors['coral']),
                              ('disabled', self.theme_colors['dark_grey'])],
                  background=[('active', self.theme_colors['dark_blue']),
                              ('pressed', self.theme_colors['coral']),
                              ('disabled', self.theme_colors['almost_black'])],
                  indicatorcolor=[('selected', self.theme_colors['coral']),
                                  ('pressed', self.theme_colors['coral']),
                                  ('disabled', self.theme_colors['almost_black'])])

        style.map('TCombobox',
                  foreground=[
                              ('focus', self.theme_colors['coral']),
                              ('!focus', self.theme_colors['light_blue']),
                              ('readonly', self.theme_colors['coral']),
                              ('disabled', self.theme_colors['dark_grey'])],
                  background=[('focus', self.theme_colors['coral']),
                              ('!focus', self.theme_colors['light_blue']),
                              ('readonly', self.theme_colors['dark_blue']),
                              ('disabled', self.theme_colors['almost_black'])],
                  fieldbackground=[('focus', self.theme_colors['almost_black']),
                                   ('!focus', self.theme_colors['almost_black']),
                                   ('readonly', self.theme_colors['dark_grey']),
                                   ('disabled', self.theme_colors['dark_grey'])],
                  highlightcolor=[('active', self.theme_colors['coral']),
                                  ('focus', self.theme_colors['coral']),
                                  ('!focus', self.theme_colors['coral']),
                                  ('disabled', self.theme_colors['almost_black'])],
                  bordercolor=[('active', self.theme_colors['coral']),
                               ('focus', self.theme_colors['coral']),
                               ('!focus', self.theme_colors['light_blue']),
                               ('disabled', self.theme_colors['almost_black'])],
                  troughcolor=[('active', self.theme_colors['coral']),
                               ('focus', self.theme_colors['coral']),
                               ('!focus', self.theme_colors['light_blue']),
                               ('disabled', self.theme_colors['almost_black'])],
                  lightcolor=[('active', self.theme_colors['coral']),
                              ('focus', self.theme_colors['coral']),
                              ('!focus', self.theme_colors['light_blue']),
                              ('disabled', self.theme_colors['almost_black'])],
                  darkcolor=[('active', self.theme_colors['coral']),
                             ('focus', self.theme_colors['coral']),
                             ('!focus', self.theme_colors['light_blue']),
                             ('disabled', self.theme_colors['almost_black'])])

        style.map('TEntry',
                  foreground=[('focus', self.theme_colors['coral']),
                              ('!focus', self.theme_colors['light_blue']),
                              ('readonly', self.theme_colors['light_blue']),
                              ('disabled', self.theme_colors['dark_grey'])],
                  fieldbackground=[('focus', self.theme_colors['almost_black']),
                                   ('!focus', self.theme_colors['almost_black']),
                                   ('readonly', self.theme_colors['dark_grey']),
                                   ('disabled', self.theme_colors['dark_grey'])],
                  highlightcolor=[('active', self.theme_colors['coral']),
                                  ('focus', self.theme_colors['coral']),
                                  ('!focus', self.theme_colors['coral']),
                                  ('disabled', self.theme_colors['almost_black'])],
                  bordercolor=[('active', self.theme_colors['coral']),
                               ('focus', self.theme_colors['coral']),
                               ('!focus', self.theme_colors['light_blue']),
                               ('disabled', self.theme_colors['almost_black'])],
                  troughcolor=[('active', self.theme_colors['coral']),
                               ('focus', self.theme_colors['coral']),
                               ('!focus', self.theme_colors['light_blue']),
                               ('disabled', self.theme_colors['almost_black'])],
                  lightcolor=[('active', self.theme_colors['coral']),
                              ('focus', self.theme_colors['coral']),
                              ('!focus', self.theme_colors['light_blue']),
                              ('disabled', self.theme_colors['almost_black'])],
                  darkcolor=[('active', self.theme_colors['coral']),
                             ('focus', self.theme_colors['coral']),
                             ('!focus', self.theme_colors['light_blue']),
                             ('disabled', self.theme_colors['almost_black'])])
        style.map('TRadiobutton',
                  foreground=[('active', self.theme_colors['coral']),
                              ('pressed', self.theme_colors['coral']),
                              ('disabled', self.theme_colors['dark_grey'])],
                  background=[('active', self.theme_colors['dark_blue']),
                              ('pressed', self.theme_colors['coral']),
                              ('disabled', self.theme_colors['almost_black'])],
                  indicatorcolor=[('selected', self.theme_colors['coral']),
                                  ('pressed', self.theme_colors['coral']),
                                  ('disabled', self.theme_colors['almost_black'])])
        style.configure('Horizontal.TProgressbar',
                        foreground=self.theme_colors['coral'],
                        background=self.theme_colors['coral'],
                        bordercolor=self.theme_colors['light_blue'],
                        troughcolor=self.theme_colors['light_blue'],
                        lightcolor=self.theme_colors['coral'],
                        darkcolor=self.theme_colors['coral'])

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

            processing_frame = ttk.Labelframe(main_frame, text='Processing Frame')
            processing_frame.grid(column=0, row=3, padx=4, pady=4)

            self.run_button = ttk.Button(processing_frame, text='Run',
                                    command=self.run_application)
            self.run_button.grid(column=0, row=0, padx=4, pady=4)

            self.status_bar = ttk.Progressbar(processing_frame, mode='determinate',
                                              length=300)
            self.status_bar.grid(column=0, row=1, padx=4, pady=4)
            self.status_bar.columnconfigure(0, weight=1)

            self.messages_text = tk.Text(processing_frame, wrap=tk.WORD, height=15, width=100)
            self.messages_text.configure(state='disabled', background='black', foreground='#c0e0de')
            self.messages_text.grid(column=0, row=2, padx=4, pady=4, sticky='news')

        except Exception as e:
            tkMessageBox.showerror('Error', e)

    def get_input_filepath(self):
        input_filepath = tkFileDialog.askopenfilename(title='Select Input File')
        self.input_variable.set(input_filepath)

    def get_second_filepath(self):
        input_filepath = tkFileDialog.askdirectory(title='Select Input Directory')
        self.second_variable.set(input_filepath)

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
            self.messages_text.insert('end', '{}Run: {}{}\n\n'.format(
                ('=' * 5), time.strftime("%c"), ('=' * 5)))

            self.messages_text.insert('end', 'Input: {}\n\n'.format(
                self.input_variable.get()))

            self.messages_text.insert('end', 'Processing with: {}\n\n'.format(
                self.second_variable.get()))

            self.messages_text.insert('end', 'With these options: {}\n\n'.format(
                [self.radio_variable.get(), self.checkbox_variable_1.get(),
                 self.checkbox_variable_2.get(), self.checkbox_variable_3.get()]))

            self.messages_text.configure(state='disabled')
        except Exception as e:
            self.status_bar.stop()
            return e

    def run_application(self):
        try:
            self.run_button.configure(state='disabled')
            self.clear_messages()
            self.status_bar.start()
            self.write_start_message()
            self.thread = ThreadedClient(self.queue, self.input_variable.get(),
                                         self.second_variable.get())
            self.thread.start()
            self.periodiccall()

        except Exception as e:
            self.status_bar.stop()
            return e

    def periodiccall(self):
        self.checkqueue()
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

    def __init__(self, queue, input_1, input_2):
        threading.Thread.__init__(self)
        self.queue = queue
        self.input_1 = input_1
        self.input_2 = input_2

    def run(self):
        time.sleep(2)
        message = "\nNow running with input: {}\nand second input: {}\n".format(
            self.input_1, self.input_2)
        self.queue.put(message)
        for x in range(1, 5):
            time.sleep(2)
            msg = "Function {} finished...\n".format(x)
            self.queue.put(msg)

if __name__ == '__main__':
    app = MainApplication(None)
    app.mainloop()
