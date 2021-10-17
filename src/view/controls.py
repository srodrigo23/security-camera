import tkinter as tk

from tkinter import LabelFrame, Label
from tkinter.ttk import Combobox, Button

class Controls(LabelFrame):
    
    def __init__(self, parent, controller):
        tk.LabelFrame.__init__(self, parent)
        self.__title__ = 'Controls'
        self.__controller__ = controller
        self.setup_controls()
    
    
    def setup_controls(self):
        self.config(text=self.__title__)

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.columnconfigure(3, weight=1)
        # self.rowconfigure(0, weight=1)
        # self.rowconfigure(1, weight=1)
        
        self.__btn_camera__ = Button(self, compound='left', text='Launch Camera', command=self.__controller__.launch_webcamera)
        self.__btn_camera__.grid(row=0, column=0, rowspan=1, columnspan=2, padx=2, pady=2, sticky='ew')
        
        self.__btn_pi_camera__ = Button(self, compound = 'left', text = 'Launch PiCamera', command=lambda: print('llega'))
        self.__btn_pi_camera__.grid(row=1, column=0, rowspan=1, columnspan=2, padx=2, pady=2, sticky='ew')
        
        self.__btn_video__ = Button(self, compound='left', text='Launch Video', 
                               command=lambda: print('llega')
                               )
        self.__btn_video__.grid(row=1, column=2, rowspan=1, columnspan=2, padx=2, pady=2, sticky='ew')
        
        __lbl_source__ = Label(self, text='Source :')
        __lbl_source__.grid(row=0, column=2, padx=2, pady=2)
        
        __videos__ = ['A', 'B', 'C']
        __cbx_video_source__ = Combobox(self, state='readonly', values=__videos__, width=10)
        __cbx_video_source__.current(0)
        __cbx_video_source__.grid(row=0, column=3, padx=2, pady=2, sticky='ew')
        
    def enable_btn_camera(self):
        self.__btn_camera__.config(state='normal')
    
    def diasble_btn_camera(self):
        self.__btn_camera__.config(state='disable')