import tkinter as tk

from PIL import ImageTk, Image
from tkinter import PhotoImage, LabelFrame, Canvas, Listbox, Label, Frame

class Screen(LabelFrame):
    """
    Screen Label Frame to show frames on the screen
    """
    def __init__(self, parent):
        """
        Init Screen to show frames
        """
        tk.LabelFrame.__init__(self, parent)
        self.__message__ = "Screen"
        self.setup_screen()
        
    def setup_screen(self):
        """
        Init screen  to show frames
        """
        self.config(text=self.__message__)
        self.__canvas__ = Canvas(self, width=320, height=240)
        self.__canvas__.pack(side='top', expand='1', fill='both')
        self.show_init_frame()
    
    def show_frame(self, frame):
        """
        Method to show frames on the screen
        """
        self.__picture__ = ImageTk.PhotoImage(image=Image.fromarray(frame))
        self.__canvas__.create_image(7, 0, image=self.__picture__, anchor='nw')
        # self.after(1, self.update_frame
    
    def show_init_frame(self):  # Get a frame from the video source
        """
        Show to image in the inital and end of playsource
        """
        self.__picture__ = ImageTk.PhotoImage(image=Image.open('img/camera.jpg'))
        self.__canvas__.create_image(7, 0, image=self.__picture__, anchor='nw')