import tkinter as tk

from PIL import ImageTk, Image
from tkinter import PhotoImage, LabelFrame, Canvas, Listbox, Label, Frame

class Screen(LabelFrame):
    
    def __init__(self, parent):
        """
            Init Screen to show frames
        """
        tk.LabelFrame.__init__(self, parent)
        self.__message__ = "Screen"
        self.setup_screen()
        
    def setup_screen(self):
        self.config(text=self.__message__)
        self.__canvas__ = Canvas(self, width=320, height=240)
        self.__canvas__.pack(side='top', expand='1', fill='both')
        self.__picture__ = ImageTk.PhotoImage(image=Image.open('img/camera.jpg'))
        self.__canvas__.create_image(7, 0, image=self.__picture__, anchor='nw')
        # self.update_frame()
    
    def update_frame(self):  # Get a frame from the video source
        # __frame__ = self.controller.get_frame()
        __picture__ = ImageTk.PhotoImage(image=Image.open('img/camera.jpg'))
        # __picture__ = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(__frame__))
        self.__canvas__.create_image(0, 0, image=__picture__, anchor=tk.NW)
        self.after(1, self.update_frame)
