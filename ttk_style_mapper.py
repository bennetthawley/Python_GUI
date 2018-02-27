import csv
import pprint
from tkinter import ttk

widgets = {'TButton': ['Button.button', 'Button.padding', 'Button.label'],
           'TCheckbutton': ['Checkbutton.padding', 'Checkbutton.label'],
           'TCombobox': ['Combobox.padding', 'Combobox.textarea'],
           'TEntry': ['Entry.field', 'Entry.padding', 'Entry.textarea'],
           'TLabel': ['Label.border', 'Label.padding', 'Label.label'],
           'TMenubutton': ['Menubutton.padding', 'Menubutton.label'],
           'TRadiobutton': ['Radiobutton.padding', 'Radiobutton.label'],
           'Horizontal.TScale': ['Horizontal.Scale.trough'],
           'Vertical.TScale': ['Vertical.Scale.trough'],
           'Horizontal.TScrollbar': ['Horizontal.Scrollbar.trough', 'Horizontal.Scrollbar.leftarrow',
                                     'Horizontal.Scrollbar.rightarrow', 'Horizontal.Scrollbar.thumb'],
           'Vertical.TScrollbar': ['Vertical.Scrollbar.trough', 'Vertical.Scrollbar.uparrow',
                                   'Vertical.Scrollbar.downarrow', 'Horizontal.Scrollbar.thumb'],
           'Treeview': ['Treeview.field', 'Treeview.padding']}

style = ttk.Style()


def print_elements(widget):
    layout = style.layout(widget)
    return layout


def print_options(element):
    options = style.element_options(element)
    return options


def write_csv(name):
    with open(name, 'w') as csvfile:
        fieldnames = ['Widget', 'Element', 'Options']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for key in widgets.keys():
            for value in widgets[key]:
                element_options = print_options(value)
                writer.writerow({fieldnames[0]: key, fieldnames[1]: value, fieldnames[2]: element_options})


pprint.pprint(print_elements('TButton'))
write_csv('ttk_style_options.csv')
