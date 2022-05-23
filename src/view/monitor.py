import tkinter as tk

from .screen import Screen
from .controls import Controls
from .connection import Connection
from .messages import Messages

from tkinter.ttk import Button

class Monitor(tk.Tk):
    """
    Class to view a monitor to show frames
    """
    def __init__(self, controller):
        """
        Init class with a screen controller and settings
        """
        super().__init__()
        self.__width__ = 584
        self.__height__ = 370
        self.__title__ = 'Node'
        self.__resizable__ = True
        self.__controller__ = controller # controller
        
        self.setup()
        
        self.setup_controls(self.__controller__.get_controls_controller())
        self.setup_connection(self.__controller__.get_connection_controller())
        self.setup_messages()
        self.setup_exit_menu()
        self.setup_screen()
                
    def setup(self):
        """
        Method to set config about layout
        """
        self.title(self.__title__)
        self.geometry(f'{self.__width__}x{self.__height__}')
        self.resizable(self.__resizable__, self.__resizable__)

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.columnconfigure(3, weight=1)
        
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        self.rowconfigure(3, weight=1)
        
    def setup_screen(self):
        """
        Method to Set screen to show frames
        """
        self.__screen__ = Screen(self)
        self.__screen__.grid(row=0, column=0, rowspan=2, columnspan=2, padx=5, pady=5, sticky='news')

    def setup_controls(self, controls_controller):
        """
        Method to setup controls of screen. open video or open camera
        """
        self.__controls__ = Controls(self, controls_controller)
        self.__controls__.grid(row=2, column=0, rowspan=2, columnspan=2, padx=5, pady=5, sticky='new')

    def setup_connection(self, connection_controller):
        """
        Method to setup connection on the main window
        """
        self.__connection__ = Connection(self, connection_controller)
        self.__connection__.grid(row=0, column=2, rowspan=1, columnspan=2, pady=5, padx=5, sticky='new')

    def setup_messages(self):
        """
        Method to set messages screen to main window
        """
        self.__messages__ = Messages(self)
        self.__messages__.grid(row=1, column=2, rowspan=2, columnspan=2, padx=5, pady=5, sticky='news')
    
    def get_screen(self):
        """
        Method to return Screen
        """
        return self.__screen__
    
    def get_controls_view(self):
        """
        Method to return controls
        """
        return self.__controls__
    
    def get_connection_view(self):
        """
        Method to return Connection view
        """
        return self.__connection__
    
    def get_messages_view(self):
        """
        Method to return Messages view
        """
        return self.__messages__
    
    def get_screen_view(self):
        """
        Method to return Screen view
        """
        return self.__screen__
    
    def setup_exit_menu(self):
        """
        Setup on the menubar with menu exit
        """
        self.__menubar__ = tk.Menu(self)
        self.config(menu=self.__menubar__)
        file_menu = tk.Menu(self.__menubar__)
        file_menu.add_command(label='Exit', command=self.destroy)
        self.__menubar__.add_cascade(label='File', menu=file_menu)
