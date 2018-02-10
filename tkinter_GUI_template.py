# import tkinter and rename to 'tk' for easier use
import tkinter as tk
# import ttk, giving access to additional fun widgets
from tkinter import ttk

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
        pass

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