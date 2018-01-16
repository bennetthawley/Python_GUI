import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import Menu
win = tk.Tk()
win.title('Python GUI')
# win.resizable(0,0)

monty = ttk.LabelFrame(win, text=' Monty Python')
monty.grid(column=0, row=0)

# Modify adding a Label
a_label = ttk.Label(monty, text=' ')
a_label.grid(column=0, row=0)


# Button Click Event Function
def click_me():
    action.configure(text='Hello ' + name.get() + ' ' + number_chosen.get())


# Change our Label
ttk.Label(monty, text='Enter a name:').grid(column=0, row=0, sticky='W')

# Adding a Textbox Entry widget
name = tk.StringVar()
name_entered = ttk.Entry(monty, width=12, textvariable=name)
name_entered.grid(column=0, row=1,sticky=tk.W)

# Adding a Button
action = ttk.Button(monty, text='Click Me!', command=click_me)
action.grid(column=2, row=1)

ttk.Label(monty, text='Choose a number:').grid(column=1, row=0)
number = tk.StringVar()
number_chosen = ttk.Combobox(monty, width=12, textvariable=number, state='readonly')
number_chosen['values'] = (1, 2, 4, 42, 100)
number_chosen.grid(column=1, row=1)
number_chosen.current(0)

# Creating three checkbuttons
check_variable_disabled = tk.IntVar()
check_1 = tk.Checkbutton(monty, text="Disabled", variable=check_variable_disabled, state='disabled')
check_1.select()
check_1.grid(column=0, row=4, sticky=tk.W)

check_variable_unchecked = tk.IntVar()
check_2 = tk.Checkbutton(monty, text="Unchecked", variable=check_variable_unchecked)
check_2.deselect()
check_2.grid(column=1, row=4, sticky=tk.W)

check_variable_enabled = tk.IntVar()
check_3 = tk.Checkbutton(monty, text='Enabled', variable=check_variable_enabled)
check_3.select()
check_3.grid(column=2, row=4, sticky=tk.W)

# Using scrolled text control
scroll_width = 30
scroll_height = 3
scroll = scrolledtext.ScrolledText(monty, width=scroll_width, height=scroll_height, wrap=tk.WORD)
scroll.grid(column=0, columnspan=3)

colors = ['Blue', 'Gold', 'Red']


# Radiobutton callback
def radio_call():
    radio_select = radio_variable.get()
    if radio_select == 0:
        monty.configure(background=colors[0])
    elif radio_select == 1:
        monty.configure(background=colors[1])
    elif radio_select == 2:
        monty.configure(background=colors[2])


# Create three Radiobuttons using one variable
radio_variable = tk.IntVar()

# Select a non-existing index value for radio_variable
radio_variable.set(99)

# Create all Radiobutton widgets within one loop
for column in range(3):
    #cur_radio = 'radio' + str(column)
    cur_radio = tk.Radiobutton(monty, text=colors[column], variable=radio_variable, value=column, command=radio_call)
    cur_radio.grid(column=column, row=6, sticky=tk.W)

# Create a container to hold labels
labels_frame = ttk.LabelFrame(monty, text=' Labels in a Frame ')
labels_frame.grid(column=0, row=7, padx=20, pady=40)

# Place labels into the container element
ttk.Label(labels_frame, text='Label 1').grid(column=0, row=0)
ttk.Label(labels_frame, text='Label 2').grid(column=0, row=1)
ttk.Label(labels_frame, text='Label 3').grid(column=0, row=2)

for child in labels_frame.winfo_children():
    child.grid_configure(padx=8, pady=4)

def _quit():
    win.quit()
    win.destroy()
    exit()

# Create a menu bar
menu_bar = Menu(win)
win.config(menu=menu_bar)

# Add menu items
file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label='New')
file_menu.add_separator()
file_menu.add_command(label='Exit', command=_quit)
menu_bar.add_cascade(label='File', menu=file_menu)

help_menu = Menu(menu_bar, tearoff=0)
help_menu.add_command(label='About')
menu_bar.add_cascade(label='Help', menu=help_menu)


name_entered.focus()

monty.mainloop()
