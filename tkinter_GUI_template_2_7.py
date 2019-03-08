import Tkinter as tk
import threading
import time
import ttk
import tkMessageBox
import tkFileDialog
import tkFont
import Queue


class MainApplication(tk.Tk):

    def __init__(self, parent, *args, **kwargs):
        tk.Tk.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.queue = Queue.Queue()
        self.input_variable = tk.StringVar()
        self.input_variable.set(' <Select a file> ')
        self.second_variable = tk.StringVar()
        self.second_variable.set(' <Select a folder> ')
        self.radio_variable = tk.StringVar()
        self.checkbox_variable_1 = tk.StringVar()
        self.checkbox_variable_2 = tk.StringVar()
        self.checkbox_variable_3 = tk.StringVar()
        self.combobox_variable = tk.StringVar()
        self.combobox_variable.set('<Select Value>')
        self.configure_main_gui()
        self.create_main_widgets()
        self.style_widgets()

    def configure_main_gui(self):
        self.title('tkinter application v2.0')
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
                  background=[('focus', theme_colors['coral']),
                              ('!focus', theme_colors['light_blue']),
                              ('readonly', theme_colors['dark_blue']),
                              ('disabled', theme_colors['almost_black'])],
                  fieldbackground=[('focus', theme_colors['almost_black']),
                                   ('!focus', theme_colors['almost_black']),
                                   ('readonly', theme_colors['dark_grey']),
                                   ('disabled', theme_colors['dark_grey'])],
                  highlightcolor=[('active', theme_colors['coral']),
                                  ('focus', theme_colors['coral']),
                                  ('!focus', theme_colors['coral']),
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
                              ('disabled', theme_colors['dark_grey'])],
                  background=[('active', theme_colors['dark_blue']),
                              ('pressed', theme_colors['coral']),
                              ('disabled', theme_colors['almost_black'])],
                  indicatorcolor=[('selected', theme_colors['coral']),
                                  ('pressed', theme_colors['coral']),
                                  ('disabled', theme_colors['almost_black'])])
        style.configure('Horizontal.TProgressbar',
                        foreground=theme_colors['coral'],
                        background=theme_colors['coral'],
                        bordercolor=theme_colors['light_blue'],
                        troughcolor=theme_colors['light_blue'],
                        lightcolor=theme_colors['coral'],
                        darkcolor=theme_colors['coral'])

    def create_main_widgets(self):
        try:
            entry_fonts = 'default 16 bold'

            main_frame = ttk.Frame(self)
            main_frame.grid(column=0, row=0, sticky='nw')

            main_label = ttk.Label(main_frame, text='Main Label')
            main_label.grid(column=0, row=0, sticky='w', padx=4, pady=4)

            input_frame = ttk.Labelframe(main_frame, text='Input Frame')
            input_frame.grid(column=0, row=1, sticky='ew', padx=4, pady=4)

            input_entry = ttk.Entry(input_frame, textvariable=self.input_variable,
                                    width=90, font=entry_fonts)
            input_entry.grid(column=0, row=0, sticky='ew', padx=4, pady=4)

            input_button = ttk.Button(input_frame, text='Browse',
                                      command=self.get_input_filepath)
            input_button.grid(column=1, row=0, sticky='ew', padx=4, pady=4)

            second_frame = ttk.Labelframe(main_frame, text='Second Frame')
            second_frame.grid(column=0, row=2, sticky='ew', padx=4, pady=4)

            second_entry = ttk.Entry(second_frame, textvariable=self.second_variable,
                                     width=90, font=entry_fonts)
            second_entry.grid(column=0, row=0, sticky='ew', padx=4, pady=4)

            second_button = ttk.Button(second_frame, text='Browse',
                                       command=self.get_second_filepath)
            second_button.grid(column=1, row=0, sticky='ew', padx=4, pady=4)

            choices_frame = ttk.Labelframe(main_frame, text='Select Options')
            choices_frame.grid(column=0, row=3, sticky='ew', padx=4, pady=4)

            radio_button_1 = ttk.Radiobutton(choices_frame, text='Option 1',
                                             value='Option 1',
                                             variable=self.radio_variable)
            radio_button_1.grid(column=0, row=0, sticky='ew', padx=2, pady=2)
            radio_button_2 = ttk.Radiobutton(choices_frame, text='Option 2',
                                             value='Option 2',
                                             variable=self.radio_variable)
            radio_button_2.grid(column=0, row=1, sticky='ew', padx=2, pady=2)
            radio_button_3 = ttk.Radiobutton(choices_frame, text='Option 3',
                                             value='Option 3',
                                             variable=self.radio_variable)
            radio_button_3.grid(column=0, row=2, sticky='ew', padx=2, pady=2)

            checkbox_1 = ttk.Checkbutton(choices_frame, text='Button 1',
                                         variable=self.checkbox_variable_1,
                                         onvalue='Button_1', offvalue='')
            checkbox_1.grid(column=1, row=0, sticky='ew', padx=2, pady=2)

            checkbox_2 = ttk.Checkbutton(choices_frame, text='Button 2',
                                         variable=self.checkbox_variable_2,
                                         onvalue='Button_2', offvalue='')
            checkbox_2.grid(column=1, row=1, sticky='ew', padx=2, pady=2)

            checkbox_3 = ttk.Checkbutton(choices_frame, text='Button 3',
                                         variable=self.checkbox_variable_3,
                                         onvalue='Button_3', offvalue='')
            checkbox_3.grid(column=1, row=2, sticky='ew', padx=2, pady=2)

            combobox_1 = ttk.Combobox(choices_frame, text='<Select Option>',
                                      values=['Choice 1', 'Choice 2', 'Choice 3'],
                                      textvariable=self.combobox_variable,
                                      state='readonly',
                                      font=entry_fonts)
            combobox_1.grid(column=2, row=0, sticky='ew', padx=2, pady=2)

            self.run_button = ttk.Button(main_frame, text='Run',
                                    command=self.run_application)
            self.run_button.grid(column=0, row=4, padx=4, pady=4)

            self.processing_frame = ttk.Labelframe(main_frame, text='Processing Frame')
            self.processing_frame.grid(column=0, row=5, padx=4, pady=4)

            self.status_bar = ttk.Progressbar(self.processing_frame, mode='determinate',
                                              length=300)
            self.status_bar.grid(column=0, row=0, padx=4, pady=4)

            self.messages_text = tk.Text(self.processing_frame, wrap=tk.WORD, height=25)
            self.messages_text.configure(state='disabled')
            self.messages_text.grid(column=0, row=1, padx=4, pady=4, sticky='ew')
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
