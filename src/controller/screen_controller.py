from threading import Thread

import time

class ScreenController():
    
    def __init__(self, camera):
        self.__view__ = None
        self.__camera__ = camera
    
    def set_view(self, view):
        self.__screen_view__ = view
        
    def start_show_frames(self):
        self.__thread__ = Thread(target=self.show_frames, args=())
        self.__thread__.daemon = True
        self.__thread__.start()
    
    def show_frames(self):
        while not self.__camera__.is_none():
            time.sleep(0.2)
            frame = self.__camera__.get_frame()
            self.__screen_view__.show_frame(frame) # show frame in screen
        