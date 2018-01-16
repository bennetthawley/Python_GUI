import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext

win = tk.Tk()
win.title('Python GUI')
# win.resizable(0,0)

# Modify adding a Label
a_label = ttk.Label(win, text='A Label')
a_label.grid(column=0, row=0)


# Button Click Event Function
def click_me():
    action.configure(text='Hello ' + name.get() + ' ' + number_chosen.get())


# Change our Label
ttk.Label(win, text='Enter a name:').grid(column=0, row=0)

# Adding a Textbox Entry widget
name = tk.StringVar()
name_entered = ttk.Entry(win, width=12, textvariable=name)
name_entered.grid(column=0, row=1)

# Adding a Button
action = ttk.Button(win, text='Click Me!', command=click_me)
action.grid(column=2, row=1)

ttk.Label(win, text='Choose a number:').grid(column=1, row=0)
number = tk.StringVar()
number_chosen = ttk.Combobox(win, width=12, textvariable=number, state='readonly')
number_chosen['values'] = (1, 2, 4, 42, 100)
number_chosen.grid(column=1, row=1)
number_chosen.current(0)

# Creating three checkbuttons
check_variable_disabled = tk.IntVar()
check_1 = tk.Checkbutton(win, text="Disabled", variable=check_variable_disabled, state='disabled')
check_1.select()
check_1.grid(column=0, row=4, sticky=tk.W)

check_variable_unchecked = tk.IntVar()
check_2 = tk.Checkbutton(win, text="Unchecked", variable=check_variable_unchecked)
check_2.deselect()
check_2.grid(column=1, row=4, sticky=tk.W)

check_variable_enabled = tk.IntVar()
check_3 = tk.Checkbutton(win, text='Enabled', variable=check_variable_enabled)
check_3.select()
check_3.grid(column=2, row=4, sticky=tk.W)

COLOR_1 = 'Blue'
COLOR_2 = 'Gold'
COLOR_3 = 'Red'


# Radiobutton callback
def radio_call():
    radio_select = radio_variable.get()
    if radio_select == 1:
        win.configure(background=COLOR_1)
    elif radio_select == 2:
        win.configure(background=COLOR_2)
    elif radio_select == 3:
        win.configure(background=COLOR_3)


# Create three Radiobuttons using one variable
radio_variable = tk.IntVar()
radio_1 = tk.Radiobutton(win, text=COLOR_1, variable=radio_variable, value=1, command=radio_call())
radio_1.grid(column=0, row=5, sticky=tk.W, columnspan=3)

radio_2 = tk.Radiobutton(win, text=COLOR_2, variable=radio_variable, value=2, command=radio_call())
radio_2.grid(column=1, row=5, sticky=tk.W, columnspan=3)

radio_3 = tk.Radiobutton(win, text=COLOR_3, variable=radio_variable, value=3, command=radio_call())
radio_3.grid(column=2, row=5, sticky=tk.W, columnspan=3)

# Using a scroll text widget
SCROLL_WIDTH = 30
SCROLL_HEIGHT = 3
scroll = scrolledtext.ScrolledText(win, width=SCROLL_WIDTH, height=SCROLL_HEIGHT, wrap=tk.WORD)
scroll.grid(column=0, columnspan=3)

name_entered.focus()

win.mainloop()
