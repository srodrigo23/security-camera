from .socket_controller import SocketController
from .controls_controller import ControlsController

class Controller():
    
    def __init__(self):
        self.__view__ =  None
        
        self.__socket_controller__ = SocketController()
        self.__controls_controller__ = ControlsController()
        
    def get_socket_controller(self):
        return self.__socket_controller__
    
    def get_controls_controller(self):
        return self.__controls_controller__
    
    def set_view(self, view):
        self.__view__ = view
        self.__controls_controller__.set_view(view.get_controls_view())
        # self.__socket_controller__.set_view(self.__view__.get)
    