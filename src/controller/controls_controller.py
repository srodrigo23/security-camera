

class ControlsController():
    
    def __init__(self):
        self.__view__ = None
        
        self.__is_on__ = False
        
    
    def set_view(self, view):
        self.__controls_view__ = view
        
    def launch_webcamera(self):
        print('llega aqui y es importante')
        if self.__is_on__:
            self.__controls_view__.disable_btn_camera()
        
        
    
    