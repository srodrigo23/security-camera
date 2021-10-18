import tkinter as tk
from tkinter.ttk import Scrollbar

from tkinter import LabelFrame, Listbox


class Messages(LabelFrame):
    """
    docstring
    """
    def __init__(self, parent):
        tk.LabelFrame.__init__(self, parent)
        self.__title__ = "Messages"
        
        self.setup_messages()
    
    
    def setup_messages(self):
        
        self.config(text=self.__title__)
        
        __scroll_bar__ = Scrollbar(self, orient='vertical')
        self.__lst_messages__ = Listbox(self, yscrollcommand=__scroll_bar__.set)
        
        self.__lst_messages__['selectforeground'] = "#ffffff"
        self.__lst_messages__['selectbackground'] = "#00aa00"
        self.__lst_messages__['selectborderwidth'] = 1
        
        self.__lst_messages__.configure(exportselection=False)
        
        __scroll_bar__.config(command=self.__lst_messages__.yview)
        __scroll_bar__.pack(side='right', fill='x')
        self.__lst_messages__.pack(expand=0, fill='x', padx=1)
