import tkinter as tk

# Create instance of tkinter
win = tk.Tk()

# Assign tkinter variable to strData variable
string_data = tk.StringVar()

# Set string_data variable
string_data.set('Hello StringVar')

# Get value of string_data variable
var_data = string_data.get()

# Print out current value of string_data
print(var_data)
