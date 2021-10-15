import tkinter as tk
import PIL.ImageTk
import PIL.Image

from tkinter import PhotoImage, LabelFrame, Canvas, Listbox, Label, Frame


class Screen(LabelFrame):
    
    def __init__(self, parent):
        """
            Init Screen to show frames
        """
        tk.LabelFrame.__init__(self, parent)
        self.__message__ = "Pantala"
        
        self.setup_screen()
        
    def setup_screen(self):
        self.config(text=self.__message__)
        __canvas__ = Canvas(self, width=320, height=180)
        __canvas__.pack(side='top', expand='1', fill='both')
    
        # self.update_frame()
    
    def update_frame(self):  # Get a frame from the video source
        
        __frame__ = self.controller.get_frame()
        __picture__ = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(__frame__))
        __canvas__.create_image(0, 0, image=__picture__, anchor=tk.NW)
        
        # self.after(50, self.update_frame)
