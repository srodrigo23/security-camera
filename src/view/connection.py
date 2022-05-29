import tkinter as tk
import settings as s

from tkinter import LabelFrame, Label, messagebox
from tkinter.ttk import Button, Entry
import settings as s

class Connection(LabelFrame):
    """ Connection class view to show connection info """
    
    def __init__(self, parent, controller):
        """ Method to init connection receive parent, controller settings """
        tk.LabelFrame.__init__(self, parent)
        self.__title__ = 'Connection'
        self.__controller__ = controller
        self.setup_connection()

    def setup_connection(self):
        """ Method to setup connection view on the screen with settings info """
        self.config(text=self.__title__)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)

        __lbl_ip__ = Label(self, text='IP :')
        __lbl_port__ = Label(self, text='Port :')
        __lbl_cam_id__ = Label(self, text='ID Cam :')
        
        self.__ent_ip__ = Entry(self, width=15)
        self.__ent_ip__.insert(0, s.get_host())
        self.__ent_port__ = Entry(self, width=15)
        self.__ent_port__.insert(0, s.get_port())
        self.__ent_cam_id__ = Entry(self, width=15)
        self.__ent_cam_id__.insert(0, s.get_cam_id())
        
        __lbl_ip__.grid(row=0, column=0, padx=2, pady=2, sticky='e')
        __lbl_port__.grid(row=1, column=0, padx=2, pady=2, sticky='e')
        __lbl_cam_id__.grid(row=2, column=0, padx=2, pady=2, sticky='e')
        
        self.__ent_ip__.grid(row=0, column=1, padx=2, pady=2)
        self.__ent_port__.grid(row=1, column=1, padx=2, pady=2)
        self.__ent_cam_id__.grid(row=2, column=1, padx=2, pady=2)

        self.__btn_connect__ = Button(self, text ='Connect', command=self.__controller__.connect_to_server)
        self.__btn_connect__.grid(row=3, column=0, columnspan=2, sticky='ew' )

    def enable_btn_connect(self):
        """ Method to enable button connect """
        self.__btn_connect__.config(state='normal')
    
    def disable_btn_connect(self):
        """ Method to disable button connect """
        self.__btn_connect__.config(state='disable')
    
    def enable_ent_ip(self):
        """ Method to enable input ip """
        self.__ent_ip__.config(state='normal')
    
    def disable_ent_ip(self):
        """ Method to disable input ip """
        self.__ent_ip__.config(state='disable')
    
    def enable_ent_port(self):
        """ Method to enable input port """
        self.__ent_port__.config(state='normal')

    def disable_ent_port(self):
        """ Method to disable input port """
        self.__ent_port__.config(state='disable')

    def enable_ent_cam_id(self):
        """ Method to enable input ip """
        self.__ent_cam_id__.config(state='normal')

    def disable_ent_cam_id(self):
        """ Method to disable input ip """
        self.__ent_cam_id__.config(state='disable')

    def enable_btn_connect(self):
        """ Method to enable button connect """
        self.__btn_connect__.config(state="normal")
    
    def disable_btn_connect(self):
        """ Method to disable button connect """
        self.__btn_connect__.config(state="disable")
    
    def set_label_btn_connect(self, text):
        """
        Method to set label text on button connect
        """
        self.__btn_connect__.config(text=text)
    
    def get_connection_info(self):
        """
        Method to get connection info on the screen
        """
        return (None if self.__ent_ip__.get() == '' else self.__ent_ip__.get(), 
                None if self.__ent_port__.get() == '' else self.__ent_port__.get(),
                None if self.__ent_cam_id__.get() == '' else self.__ent_cam_id__.get())
    
    def show_alert_message(self, text):
        """
        Method to show alert message
        """
        messagebox.showerror(title='Connecting Error', message=text)
