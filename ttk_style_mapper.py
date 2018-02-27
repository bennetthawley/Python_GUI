import tkinter
from tkinter import ttk
import pprint
import json

_widgets = ['TCombobox', 'TEntry', 'TFrame', 'TLabel', 'TLabelFrame','TMenubutton',
           'TNotebook', 'TPanedwindow', 'Horizontal.TProgressbar', 'Vertical.TProgressbar', 'TRadiobutton',
           'Horizontal.TScale', 'Vertical.TScale', 'Horizontal.TScrollbar', 'Vertical.Scrollbar', 'TSeparator',
           'TSizegrip', 'Treeview']

widgets = {'TButton':['Button.padding','Button.label'],
           'TCheckbutton':['Checkbutton.padding', 'Checkbutton.label']}

style = ttk.Style()

def print_elements(widget):
    layout = style.layout(widget)
    pprint.pprint(layout)

def print_options(element):
    options = style.element_options(element)
    pprint.pprint(options)

for key in widgets.keys():
    print(key)
    for value in widgets[key]:
        print(value)
        print_options(value)



