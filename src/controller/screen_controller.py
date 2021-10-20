from threading import Thread

import time

class ScreenController():
    
    def __init__(self, camera):
        self.__view__ = None
        self.__camera__ = camera
        
    def set_view(self, view):
        self.__screen_view__ = view
    
    def set_controls_controller(self, controls_controller):
        self.__controls_controller__ = controls_controller 
        
    def start_show_frames(self):
        self.__thread__ = Thread(target=self.show_frames, args=())
        self.__thread__.daemon = True
        self.__thread__.start()
    
    def show_frames(self):
        while True:
            time.sleep(0.5)
            if not self.__camera__.is_none():
                frame = self.__camera__.get_frame()
                if not frame is None:
                    self.__screen_view__.show_frame(frame) # show frame in screen
            else:
                break
        self.__screen_view__.show_init_frame()
        self.__controls_controller__.enable_behaviour_launch_video()
