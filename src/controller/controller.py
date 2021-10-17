from .connection_controller import ConnectionController
from .controls_controller import ControlsController

class Controller():
    
    def __init__(self):
        self.__view__ =  None
        
        self.__connection_controller__ = ConnectionController()
        self.__controls_controller__ = ControlsController()
        
    def get_connection_controller(self):
        return self.__connection_controller__
    
    def get_controls_controller(self):
        return self.__controls_controller__
    
    def set_view(self, view):
        self.__view__ = view
        self.__controls_controller__.set_view(view.get_controls_view())
        self.__connection_controller__.set_view(view.get_connection_view())
    