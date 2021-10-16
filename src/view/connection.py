import tkinter as tk

from tkinter import LabelFrame, Label
from tkinter.ttk import Button, Entry

class Connection(LabelFrame):
    
    
    def __init__(self, parent):
        tk.LabelFrame.__init__(self, parent)
        self.__title__ = 'Connection'

        self.setup_connection()

    def setup_connection(self):
        self.config(text=self.__title__)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)

        __lbl_ip__ = Label(self, text='IP')
        __lbl_port__ = Label(self, text='Port')
        
        __ent_ip__ = Entry(self, width=15)
        __ent_port__ = Entry(self, width=15)
        
        __lbl_ip__.grid(row=0, column=0, padx=2, pady=2, sticky='e')
        __lbl_port__.grid(row=1, column=0, padx=2, pady=2, sticky='e')
        
        __ent_ip__.grid(row=0, column=1, padx=2, pady=2)
        __ent_port__.grid(row=1, column=1, padx=2, pady=2)

        __btn_connect__ = Button(self, text ='Connect')
        __btn_connect__.grid(row=2, column=0, columnspan=2, sticky='ew' )
