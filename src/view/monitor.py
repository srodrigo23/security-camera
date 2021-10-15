import tkinter as tk

from .screen import Screen
from .source import Source

class Monitor(tk.Tk):
    
    """
        Class to view a monitor to show frames
    """

    def __init__(self):
        super().__init__()
        
        self.__width__ = 450
        self.__height__ = 300
        self.__title__ = 'Node'
        self.__resizable__ = False
        
        self.setup()
        self.setup_screen()
        self.setup_source()
        
                
    def setup(self):
        self.title(self.__title__)
        self.geometry(f'{self.__width__}x{self.__height__}')
        self.resizable(self.__resizable__, self.__resizable__)
    
    def setup_screen(self):
        __screen__ = Screen(self)
        __screen__.pack(side='left', fill='both', expand=1, padx=5, pady=5)

    def setup_source(self):
        __source__ = Source(self)
        __source__.pack(side='right', fill='both', expand=1, padx=5, pady=5)
