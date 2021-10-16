import tkinter as tk
from tkinter import LabelFrame, Radiobutton, StringVar

class Options(LabelFrame):
    """
    docstring
    """
    def __init__(self, parent):
        """
            Init Options component
        """
        tk.LabelFrame.__init__(self, parent)        
        self.__title__ = 'Options'
        self.__option__ = StringVar(value='cam')
        
        self.setup_options()
    
    
    def setup_options(self):
        self.config(text=self.__title__)
        __rdb_camera__ = Radiobutton(self, text='Camera', variable=self.__option__, value='cam', 
                                    #  command = 
                                     )
        __rdb_video__ = Radiobutton(
            self, text='Video', variable=self.__option__, value='vid', 
            #command=
            )
        __rdb_camera__.pack(side='top', fill='both')
        __rdb_video__.pack(side='top', fill='both')
    