# import tkinter and rename to 'tk' for easier use
import tkinter as tk

''' Create the class 'SimpleApp' to house the main application. Inherit the 
base class behaviour of tk.Tk by entering "tk.Tk" in the parenthesis of the 
class. This can be changed to ttk.Frame to inherit different 
behaviour if needed.'''


class SimpleApp(tk.Tk):
    ''' Create the 'Constructor' (__init__) method using 'def __init__'
    Create (self, parent) parameters for constructor method
    This __init__ method is used when an instance of SimpleApp is created
    or "instantiated" '''

    def __init__(self, parent):
        ''' Call the base __init__ method inherited from tk.Tk using the
        self and parent parameters. '''
        tk.Tk.__init__(self, parent)
        ''' Access the application's parent attribute (currently None) 
        and set it equal to the "parent" parameter. This stores a reference to
        the parent object for tracking purposes '''
        self.parent = parent
        ''' Call the application's initialize method (defined later) to create
        all the GUI elements. GUI elements include buttons, frames, 
        entry widgets, and others '''
        self.initialize()

    ''' Define a method 'initialize' that creates all the GUI elements. 
    Provide 'self' (the application base tk.Tk constructor) as the input parameter '''

    def initialize(self):
        # Use "grid" layout style to place widgets in main application window.
        self.grid()

        ''' Add a text entry widget, named "entry" and place it in the window grid. 
        Use "self.entry" to save a reference to "entry" within the application
        so that the entry widget can be accessed outside of the initialize method. '''
        self.entry_variable = tk.StringVar()
        self.entry = tk.Entry(self, textvariable=self.entry_variable)
        self.entry.grid(column=0, row=0, sticky='EW')
        # Set a 'bind' method on the entry box to call the on_press_enter method
        self.entry.bind('<Return>', self.on_press_enter)
        # Set the tkinter string variable 'entry_variable' to a text string
        self.entry_variable.set('Enter text here')

        '''Add a button widget, place it in the window, and set the command to
        run the 'on_button_click' method when clicked'''
        button = tk.Button(self, text="Button", command=self.on_button_click)
        button.grid(column=1, row=0)

        # Create a tkinter string variable to use later
        self.label_variable = tk.StringVar()
        ''' Add a label widget, set its value to the tkinter string variable, 
        and place it in the window with white font and blue background'''
        label = tk.Label(self, textvariable=self.label_variable,
                         anchor='w', fg='white', bg='blue')
        label.grid(column=0, row=1, columnspan=2, sticky='EW')
        # Set the tkinter string variable 'label_variable' to a text string
        self.label_variable.set('Hello')

        # Enable resizing of column 0 when the window is resized by user
        self.grid_columnconfigure(0, weight=1)

        # Restrict window resizing to only horizontal
        self.resizable(width=True, height=False)
        # Update the GUI window to refresh any widget content
        self.update()
        # Set the size of the GUI to the initial needed size of the GUI
        self.geometry(self.geometry())
        # Set the cursor focus to the entry widget
        self.entry.focus_set()
        self.entry.selection_range(0, tk.END)

    def on_button_click(self):
        self.label_variable.set(self.entry_variable.get() + " You clicked the button")
        self.entry.focus_set()
        self.entry.selection_range(0, tk.END)

    def on_press_enter(self):
        self.label_variable.set(self.entry_variable.get() + " You pressed enter!")
        self.entry.focus_set()
        self.entry.selection_range(0, tk.END)


# Execute a 'main' when the program is run
if __name__ == '__main__':
    ''' Instantiate (create an instance of) the SimpleApp class. 
    Provide a "None" parent parameter, because it is the first/main GUI element.
    Save the instance of SimpleApp to the variable "app" '''
    app = SimpleApp(None)
    # Set the title of the new application
    app.title('My Application')
    ''' Set the application to wait or "listen" for events, such as user
    interaction like a button click or a key press. '''
    app.mainloop()
