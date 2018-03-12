import tkinter as tk
from tkinter import ttk
import threading
import queue
import time


class App(tk.Tk):

    def __init__(self):
        tk.Tk.__init__(self)
        self.queue = queue.Queue()
        self.style_widgets()
        main_frame = ttk.Labelframe(self, text='Main Frame')
        main_frame.grid(column=0, row=0)

        self.listbox = tk.Listbox(main_frame, width=20, height=5)
        self.progressbar = ttk.Progressbar(main_frame, orient='horizontal',
                                           length=300, mode='determinate')
        self.button = ttk.Button(main_frame, text="Start", command=self.spawnthread)
        self.listbox.pack(padx=10, pady=10)
        self.progressbar.pack(padx=10, pady=10)
        self.button.pack(padx=10, pady=10)

    def style_widgets(self):
        theme_colors = {'light_blue': '#c0e0de',
                        'dark_blue': '#0d324d',
                        'dark_grey': '#2b303a',
                        'almost_black': '#100007',
                        'coral': '#ff220c'}
        style = ttk.Style(self)
        style.theme_use('clam')
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

    def spawnthread(self):
        self.button.config(state="disabled")
        self.thread = ThreadedClient(self.queue)
        self.thread.start()
        self.periodiccall()

    def periodiccall(self):
        self.checkqueue()
        if self.thread.is_alive():
            self.after(100, self.periodiccall)
        else:
            self.button.config(state="active")

    def checkqueue(self):
        while self.queue.qsize():
            try:
                msg = self.queue.get(0)
                self.listbox.insert('end', msg)
                self.progressbar.step(25)
            except Queue.Empty:
                pass


class ThreadedClient(threading.Thread):

    def __init__(self, queue):
        threading.Thread.__init__(self)
        self.queue = queue

    def run(self):
        for x in range(1, 5):
            time.sleep(2)
            msg = "Function %s finished..." % x
            self.queue.put(msg)


if __name__ == "__main__":
    app = App()
    app.mainloop()