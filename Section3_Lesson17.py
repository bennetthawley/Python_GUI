import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext

# from tkinter import Menu

win = tk.Tk()
win.title('Python GUI')

# Tab control introduced here -------------------

# Create tab control
tab_control = ttk.Notebook(win)
# Create a tab
tab_1 = ttk.Frame(tab_control)
# Add the tab
tab_control.add(tab_1, text='Tab 1')
# Create a tab
tab_2 = ttk.Frame(tab_control)
# Add the tab
tab_control.add(tab_2, text='Tab 2')
# Pack to make visible
tab_control.pack(expand=1, fill='both')

# Tab control ended here      -------------------

monty = ttk.LabelFrame(tab_1, text=' Monty Python')
monty.grid(column=0, row=0)

# Modify adding a Label
a_label = ttk.Label(monty, text=' ')
a_label.grid(column=0, row=0)


# Button Click Event Function
def click_me():
    action.configure(text='Hello ' + name.get())


ttk.Label(monty, text='Enter a name:').grid(column=0, row=0, sticky='W')

# Adding a textbox entry widget
name = tk.StringVar()
name_entered = ttk.Entry(monty, width=12, textvariable=name)
name_entered.grid(column=0, row=1, sticky=tk.W)

# Adding a button
action = ttk.Button(monty, text='Click Me!', command=click_me)
action.grid(column=2, row=1)

ttk.Label(monty, text='Choose a number:').grid(column=1, row=0)
number = tk.StringVar()
number_chosen = ttk.Combobox(monty, width=12, textvariable=number)
number_chosen['values'] = (1, 2, 4, 42, 100)
number_chosen.grid(column=1, row=1)
number_chosen.current(0)


# Spinbox callback
def _spin():
    value = spin.get()
    print(value)
    scroll.insert(tk.INSERT, value + '\n')


# Adding a spinbox widget
spin = tk.Spinbox(monty, width=5, values=(1, 2, 3), bd=8, command=_spin)
spin.grid(column=0, row=2)

# Adding a second spinbox widget
spin = tk.Spinbox(monty, values=(0, 50, 100), width=5, bd=8, command=_spin, relief=tk.RIDGE)
spin.grid(column=1, row=2)

# Using a scrolled text control
scroll_w = 30
scroll_h = 3
scroll = scrolledtext.ScrolledText(monty, width=scroll_w, height=scroll_h, wrap=tk.WORD)
scroll.grid(column=0, row=3, sticky='WE', columnspan=3)
win.mainloop()
