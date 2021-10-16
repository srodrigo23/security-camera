import tkinter as tk
from tkinter import LabelFrame
from tkinter.ttk import Scrollbar, Combobox

class Source(LabelFrame):

    def __init__(self, parent):
        """
            Init Source to show 
        """
        tk.LabelFrame.__init__(self, parent)
        self.__title__ = "Source"
        
        self.setup_source()

    def setup_source(self):
        self.config(text=self.__title__)
        # __videos__, __path__ = self.controller.get_videos()
        __videos__ = ['A', 'B', 'C']
        __cbx_video_source__ = Combobox(self, state='readonly', values=__videos__)
        __cbx_video_source__.current(0)
        __cbx_video_source__.pack(side='top', fill='x', padx=10)
        
        # frm_source.pack(side='top', fill='x', expand=0, padx=5, pady=5)
