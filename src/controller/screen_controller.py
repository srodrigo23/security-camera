from threading import Thread

import time

class ScreenController():
    """
    Controller to Screen to show image start end up transmission
    """
    
    def __init__(self, camera):
        """
        MVC Pattern with view in None
        """
        self.__view__ = None
        self.__camera__ = camera
        
    def set_view(self, view):
        """
        Set view to the controller
        """
        self.__screen_view__ = view
    
    def set_controls_controller(self, controls_controller):
        """
        Set controls to control play/pause options 
        """
        self.__controls_controller__ = controls_controller 
        
    def start_show_frames(self):
        self.__thread__ = Thread(target=self.show_frames, args=())
        self.__thread__.daemon = True
        self.__thread__.start()
    
    def show_frames(self):
        """
        Infinite loop to show frames in screen 
        """
        while True:
            time.sleep(0.25)
            if not self.__camera__.is_none():
                frame = self.__camera__.get_frame()
                if not frame is None:
                    self.__screen_view__.show_frame(frame) # show frame in screen
            else:
                break
        self.__screen_view__.show_init_frame()
        self.__controls_controller__.enable_behaviour_launch_video()