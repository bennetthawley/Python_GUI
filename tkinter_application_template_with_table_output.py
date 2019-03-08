import logging
import threading
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk


class WidgetLogger(logging.Handler):
    def __init__(self, widget):
        logging.Handler.__init__(self)
        self.setLevel(logging.INFO)
        self.formatter = logging.Formatter(
            '%(asctime)s - %(levelname)s - %(message)s')
        self.widget = widget
        self.widget.config(state='disabled')

    def emit(self, record):
        self.widget.config(state='normal')
        # Append message (record) to the widget
        self.widget.insert(tk.END, self.format(record) + '\n')
        self.widget.see(tk.END)  # Scroll to the bottom
        self.widget.config(state='disabled')
        self.widget.update()

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
        self.style_widgets()

        # setting up the logger using the WidgetLogger class
        self.logger = logging.getLogger(__name__)
        text_logger = WidgetLogger(self.messages_text)
        # logging.basicConfig(filename='test.log',
        #     level=logging.INFO,
        #     format='%(asctime)s - %(levelname)s - %(message)s')

        self.logger.addHandler(text_logger)

    def configure_main_gui(self):
        self.title('tkinter application v1.0')
        self.resizable(width=False, height=False)
        self.focus_force()

    def style_widgets(self):
        theme_colors = {'Primary': '#D3DADB',
                        'Second': '#525251',
                        'Third': '#3B627E',
                        'Fourth': '#5799C3',
                        'Fifth': '#8DCFDA',
                        'Sixth': '#B7F0ED'}
        style = ttk.Style(self)
        font = 'helvetica 12 bold'
        style.configure('.', font=font,
                        foreground=theme_colors['Third'],
                        background=theme_colors['Fifth'])
        style.configure('TButton', font=font,
                        foreground=theme_colors['Third'],
                        background=theme_colors['Fifth'])
        style.configure('TEntry', font=font,
                        foreground=theme_colors['Third'],
                        background=theme_colors['Fifth'])
        style.configure('TCheckbutton', font=font,
                        foreground=theme_colors['Third'],
                        background=theme_colors['Fifth'])
        style.configure('TFrame', font=font,
                        foreground=theme_colors['Third'],
                        background=theme_colors['Fifth'])
        style.configure('TLabel', font=font,
                        foreground=theme_colors['Third'],
                        background=theme_colors['Fifth'])
        style.configure('TLabelFrame', font=font,
                        foreground=theme_colors['Third'],
                        background=theme_colors['Fifth'])
        style.configure('Horizontal.TProgressbar', font=font,
                        foreground=theme_colors['Third'],
                        background=theme_colors['Fifth'])

    def create_main_widgets(self):
        try:
            main_frame = ttk.Frame(self)
            main_frame.grid(column=0, row=0, sticky='nw')

            main_label = ttk.Label(main_frame, text='Main Label')
            main_label.grid(column=0, row=0, sticky='w', padx=4, pady=4)

            run_button = ttk.Button(main_frame, text='Run',
                                    command=self.run_application)
            run_button.grid(column=0, row=4, padx=4, pady=4)

            self.processing_frame = ttk.Labelframe(main_frame,
                                                   text='Processing Frame')
            self.processing_frame.grid(column=0, row=5, padx=4, pady=4)

            self.status_bar = ttk.Progressbar(self.processing_frame,
                                              mode='indeterminate',
                                              length=300)
            self.status_bar.grid(column=0, row=0, padx=4, pady=4)

            self.messages_text = tk.Text(self.processing_frame, wrap=tk.WORD,
                                         height=25)
            self.messages_text.configure(state='disabled')
            self.messages_text.grid(column=0, row=1, padx=4, pady=4,
                                    sticky='ew')



        except Exception as e:
            messagebox.showerror('Error', e)

    def run_application(self):
        try:
            self.main_thread = threading.Thread(target=self.processing_function)
            self.clear_messages()
            self.status_bar.start()
            self.main_thread.start()
        except Exception as e:
            self.status_bar.stop()
            self.logger.exception(e)


    def processing_function(self):
        try:
            self.write_to_messages('Process starting...\n\n')
            self.status_bar.start()

            my_dict = {}

            summary_message = self.add_to_dict(my_dict)

            self.write_to_messages(summary_message)
            self.write_to_messages('\n\nProcess has completed!')
            self.status_bar.stop()
        except Exception as e:
            self.status_bar.stop()
            self.logger.exception(e)

    def add_to_dict(self, dict):
        try:
            dict['gen15'] = ['Pass', 'Fail']
            dict['a223344'] = ['Pass', 'Fail']
            dict['h231456'] = ['Fail', 'Pass']
            dict['h224455'] = ['Pass', 'Pass']

            dict_message = "{:<8} {:<12} {:<10}".format(
                'Replica', 'Schema_Test', 'Class_Test\n')
            dict_message += '=' * 32
            for k, v in sorted(dict.items()):
                schema = v[0]
                _class = v[1]
                dict_message += "\n{:<8} {:<12} {:<10}\n".format(k, schema,
                                                                 _class)
                dict_message += '-' * 32

            return dict_message

        except Exception as e:
            self.status_bar.stop()
            self.logger.exception(e)

    def write_to_messages(self, message):
        try:
            self.messages_text.configure(state='normal')
            self.messages_text.insert('end', message)
            self.messages_text.configure(state='disabled')
        except Exception as e:
            self.status_bar.stop()
            self.logger.exception(e)


    def clear_messages(self):
        try:
            raise Exception("Stuff Happened")
            self.messages_text.configure(state='normal')
            self.messages_text.delete('1.0', tk.END)
            self.messages_text.configure(state='disabled')

        except Exception as e:
            self.status_bar.stop()
            self.logger.exception(e)


if __name__ == '__main__':
    app = MainApplication(None)
    app.mainloop()
