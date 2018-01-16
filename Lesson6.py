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

colors = ['Blue', 'Gold', 'Red']


# Radiobutton callback
def radio_call():
    radio_select = radio_variable.get()
    if radio_select == 0:
        win.configure(background=colors[0])
    elif radio_select == 1:
        win.configure(background=colors[1])
    elif radio_select == 2:
        win.configure(background=colors[2])


# Create three Radiobuttons using one variable
radio_variable = tk.IntVar()

# Select a non-existing index value for radio_variable
radio_variable.set(99)

# Create all Radiobutton widgets within one loop
for column in range(3):
    #cur_radio = 'radio' + str(column)
    cur_radio = tk.Radiobutton(win, text=colors[column], variable=radio_variable, value=column, command=radio_call)
    cur_radio.grid(column=column, row=6, sticky=tk.W)

# Using a scroll text widget
SCROLL_WIDTH = 30
SCROLL_HEIGHT = 3
scroll = scrolledtext.ScrolledText(win, width=SCROLL_WIDTH, height=SCROLL_HEIGHT, wrap=tk.WORD)
scroll.grid(column=0, columnspan=3)

name_entered.focus()

win.mainloop()
