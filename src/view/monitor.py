import tkinter as tk

from .screen import Screen
from .controls import Controls
from .connection import Connection

class Monitor(tk.Tk):
    
    """
        Class to view a monitor to show frames
    """
    def __init__(self):
        super().__init__()
        
        self.__width__ = 550
        self.__height__ = 360
        self.__title__ = 'Node'
        self.__resizable__ = True
        
        self.setup()
        self.setup_screen()
        self.setup_controls()
        self.setup_connection()
                
    def setup(self):
        self.title(self.__title__)
        self.geometry(f'{self.__width__}x{self.__height__}')
        self.resizable(self.__resizable__, self.__resizable__)

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        
    def setup_screen(self):
        __screen__ = Screen(self)
        __screen__.grid(row=0, column=0, rowspan=2, columnspan=2, padx=5, pady=5)
        # __screen__.pack(side='left', fill='x', expand=1, padx=5, pady=5)

    def setup_controls(self):
        __controls__ = Controls(self)
        __controls__.grid(row=2, column=0, rowspan=2, columnspan=2, padx=5, sticky='news')
        # __source__.pack(side='top', fill='x', expand=1, padx=5, pady=5)

    def setup_connection(self):
        __connection__ = Connection(self)
        __connection__.grid(row=0, column=2, rowspan=1,
                            columnspan=1, pady=5,padx=5, sticky='new')
        # __options__.pack(side='top', fill='x', expand=1, padx=5, pady=5)
