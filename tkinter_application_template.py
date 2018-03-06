import threading
import time
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from tkinter import ttk


class MainApplication(tk.Tk):

    def __init__(self, parent, *args, **kwargs):
        tk.Tk.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.input_variable = tk.StringVar()
        self.input_variable.set(' <Select a file> ')
        self.second_variable = tk.StringVar()
        self.second_variable.set(' <Select a folder> ')
        self.radio_variable = tk.StringVar()
        self.checkbox_variable_1 = tk.StringVar()
        self.checkbox_variable_2 = tk.StringVar()
        self.checkbox_variable_3 = tk.StringVar()

        self.configure_main_gui()
        self.create_main_widgets()



    def configure_main_gui(self):
        self.title('tkinter application v1.0')
        self.resizable(width=False, height=False)
        self.focus_force()

    def create_main_widgets(self):
        try:
            main_frame = ttk.Frame(self)
            main_frame.grid(column=0, row=0, sticky='nw')

            main_label = ttk.Label(main_frame, text='Main Label')
            main_label.grid(column=0, row=0, sticky='w', padx=4, pady=4)

            input_frame = ttk.Labelframe(main_frame, text='Input Frame')
            input_frame.grid(column=0, row=1, sticky='ew', padx=4, pady=4)

            input_entry = ttk.Entry(input_frame, textvariable=self.input_variable,
                                    width=90)
            input_entry.grid(column=0, row=0, sticky='ew', padx=4, pady=4)

            input_button = ttk.Button(input_frame, text='Browse',
                                      command=self.get_input_filepath)
            input_button.grid(column=1, row=0, sticky='ew', padx=4, pady=4)

            second_frame = ttk.Labelframe(main_frame, text='Second Frame')
            second_frame.grid(column=0, row=2, sticky='ew', padx=4, pady=4)

            second_entry = ttk.Entry(second_frame, textvariable=self.second_variable,
                                     width=90)
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


            run_button = ttk.Button(main_frame, text='Run',
                                    command=self.run_application)
            run_button.grid(column=0, row=4, padx=4, pady=4)

            self.processing_frame = ttk.Labelframe(main_frame, text='Processing Frame')
            self.processing_frame.grid(column=0, row=5, padx=4, pady=4)

            self.status_bar = ttk.Progressbar(self.processing_frame, mode='indeterminate',
                                              length=300)
            self.status_bar.grid(column=0, row=0, padx=4, pady=4)

            self.messages_text = tk.Text(self.processing_frame, wrap=tk.WORD, height=25)
            self.messages_text.configure(state='disabled')
            self.messages_text.grid(column=0, row=1, padx=4, pady=4, sticky='ew')
        except Exception as e:
            messagebox.showerror('Error', e)

    def get_input_filepath(self):
        input_filepath = filedialog.askopenfilename(title='Select Input File')
        self.input_variable.set(input_filepath)

    def get_second_filepath(self):
        input_filepath = filedialog.askdirectory(title='Select Input Directory')
        self.second_variable.set(input_filepath)

    def run_application(self):
        try:
            self.main_thread = threading.Thread(target=self.processing_function)
            self.clear_messages()
            self.status_bar.start()
            self.write_start_message()
            self.main_thread.start()
        except Exception as e:
            self.status_bar.stop()
            return e

    def processing_function(self):
        try:
            self.write_to_messages('Process starting...\n\n')
            time.sleep(5)
            self.write_to_messages('Process has completed!')
            self.status_bar.stop()
        except Exception as e:
            self.status_bar.stop()
            return e

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


if __name__ == '__main__':
    app = MainApplication(None)
    app.mainloop()
