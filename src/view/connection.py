import tkinter as tk

from tkinter import LabelFrame, Label, messagebox
from tkinter.ttk import Button, Entry

class Connection(LabelFrame):
    
    def __init__(self, parent, controller, settings):
        tk.LabelFrame.__init__(self, parent)
        self.__title__ = 'Connection'
        self.__controller__ = controller
        self.setup_connection(settings)

    def setup_connection(self, settings):
        self.config(text=self.__title__)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)

        __lbl_ip__ = Label(self, text='IP :')
        __lbl_port__ = Label(self, text='Port :')
        
        self.__ent_ip__ = Entry(self, width=15)
        self.__ent_ip__.insert(0, settings.get_host())
        self.__ent_port__ = Entry(self, width=15)
        self.__ent_port__.insert(0, settings.get_port())
        
        __lbl_ip__.grid(row=0, column=0, padx=2, pady=2, sticky='e')
        __lbl_port__.grid(row=1, column=0, padx=2, pady=2, sticky='e')
        
        self.__ent_ip__.grid(row=0, column=1, padx=2, pady=2)
        self.__ent_port__.grid(row=1, column=1, padx=2, pady=2)

        self.__btn_connect__ = Button(self, text ='Connect', command=self.__controller__.connect_to_server)
        self.__btn_connect__.grid(row=2, column=0, columnspan=2, sticky='ew' )

    def enable_btn_connect(self):
        self.__btn_connect__.config(state='normal')
    
    def disable_btn_connect(self):
        self.__btn_connect__.config(state='disable')
    
    def enable_ent_ip(self):
        self.__ent_ip__.config(state='normal')
    
    def disable_ent_ip(self):
        self.__ent_ip__.config(state='disable')
    
    def enable_ent_port(self):
        self.__ent_port__.config(state='normal')

    def disable_ent_port(self):
        self.__ent_port__.config(state='disable')
        
    def set_label_btn_connect(self, text):
        self.__btn_connect__.config(text=text)
    
    def get_connection_info(self):
        return (None if self.__ent_ip__.get() == '' else self.__ent_ip__.get(), None if self.__ent_port__.get() == '' else self.__ent_port__.get())
    
    def show_alert_message(self, text):
        messagebox.showerror(title='Connecting Error', message=text)
