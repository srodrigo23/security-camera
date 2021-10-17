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
        
        self.__btn_camera__ = Button(self, compound='left', text='Start WebCamera', command=self.__controller__.launch_webcamera)
        self.__btn_camera__.grid(row=0, column=0, rowspan=1, columnspan=2, padx=2, pady=2, sticky='ew')
        
        self.__btn_pi_camera__ = Button(self, compound = 'left', text = 'Launch PiCamera', command=self.__controller__.launch_picamera)
        self.__btn_pi_camera__.grid(row=1, column=0, rowspan=1, columnspan=2, padx=2, pady=2, sticky='ew')
        
        self.__btn_video__ = Button(self, compound='left', text='Launch Video', command=self.__controller__.launch_video)
        self.__btn_video__.grid(row=1, column=2, rowspan=1, columnspan=2, padx=2, pady=2, sticky='ew')
        
        __lbl_source__ = Label(self, text='Source :')
        __lbl_source__.grid(row=0, column=2, padx=2, pady=2)
        
        __videos__ = ['A', 'B', 'C']
        self.__cbx_video_source__ = Combobox(self, state='readonly', values=__videos__, width=10)
        self.__cbx_video_source__.current(0)
        self.__cbx_video_source__.grid(row=0, column=3, padx=2, pady=2, sticky='ew')
        
    def enable_btn_webcamera(self):
        self.__btn_camera__.config(state='normal')
    
    def disable_btn_webcamera(self):
        self.__btn_camera__.config(state='disable')
    
    def enable_btn_picamera(self):
        self.__btn_pi_camera__.config(state='normal')
        
    def disable_btn_picamera(self):
        self.__btn_pi_camera__.config(state='disable')
        
    def enable_btn_video(self):
        self.__btn_video__.config(state='normal')

    def disable_btn_video(self):
        self.__btn_video__.config(state='disable')
    
    def enable_cbx_video_source(self):
        self.__cbx_video_source__.config(state='normal')
    
    def disable_cbx_video_source(self):
        self.__cbx_video_source__.config(state='disable')
    
    def set_label_btn_webcamera(self, text):
        self.__btn_camera__.config(text=text)
    
    def set_label_btn_picamera(self, text):
        self.__btn_pi_camera__.config(text=text)
    
    def set_label_btn_video(self, text):
        self.__btn_video__.config(text=text)
