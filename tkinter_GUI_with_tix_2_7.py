import Tkinter as tk
import ttk
import Tix


class main_frame(ttk.Frame):

    def __init__(self, parent):
        ttk.Frame.__init__(self, parent)
        self.parent = parent
        self.create_main_widgets()
        #self.style_widgets()

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

    def create_main_widgets(self):

        combo_box = Tix.ComboBox(self)
        combo_box.grid(column=0, row=0)

        button_box = Tix.ButtonBox(self)
        button_box.add('button_1', text='Button_1')
        button_box.add('button_2', text='Button_2')
        button_box.grid(column=0, row=1, sticky='news')


if __name__ == '__main__':
    root = Tix.Tk()
    main_frame(root).pack()
    root.mainloop()
