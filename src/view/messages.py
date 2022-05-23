import tkinter as tk
from tkinter.ttk import Scrollbar
from threading import Thread
import time

from tkinter import LabelFrame, Listbox

class Messages(LabelFrame):
    """
    Class Messages extends from LabelFrame
    """
    def __init__(self, parent):
        """
        Method to init Messages View class
        """
        tk.LabelFrame.__init__(self, parent)
        self.__title__ = "Messages"
        self.__cnt_elements__ = 0
        self.setup_messages()
    
    def setup_messages(self):
        """
        Method to setup view components on the screen
        """
        self.config(text=self.__title__)
        
        __scroll_bar__ = Scrollbar(self, orient='vertical')
        self.__lst_messages__ = Listbox(self, yscrollcommand=__scroll_bar__.set)
        
        self.__lst_messages__['selectforeground'] = "#ffffff"
        self.__lst_messages__['selectbackground'] = "#00aa00"
        self.__lst_messages__['selectborderwidth'] = 1
        
        self.__lst_messages__.configure(exportselection=False)
        
        __scroll_bar__.config(command=self.__lst_messages__.yview)
        __scroll_bar__.pack(side='right', fill='y')
        self.__lst_messages__.pack(expand=0, fill='x', padx=1)
    
    def add_message(self, text):
        """
        Method to add a text in list to show message
        """
        # if self.__cnt_elements__ % 10 == 0:
        #     self.__lst_messages__.delete(0, 'end')
        self.__lst_messages__.insert('end', text)
        self.__cnt_elements__ += 1