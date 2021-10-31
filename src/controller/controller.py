from .connection_controller import ConnectionController
from .controls_controller import ControlsController
from .messages_controller import MessagesController
from .screen_controller import ScreenController

from model.camera import Camera
from model.connection import Connection

class Controller():
    
    def __init__(self):
        self.__view__ =  None
    
        self.__messages_controller__   = MessagesController()
        
        self.__camera__ = Camera()
        self.__connection__ = Connection(camera=self.__camera__, messages=self.__messages_controller__)
        
        self.__connection_controller__ = ConnectionController(self.__connection__, self.__messages_controller__)
        self.__screen_controller__     = ScreenController(self.__camera__)
        self.__controls_controller__   = ControlsController(self.__camera__, self.__screen_controller__)
        
        self.__screen_controller__.set_controls_controller(self.__controls_controller__)
        
    
    def get_connection_controller(self):
        return self.__connection_controller__
    
    def get_controls_controller(self):
        return self.__controls_controller__
    
    def get_messages_controller(self):
        return self.__messages_controller__
    
    def get_screen_controller(self):
        return self.__screen_controller__
    
    def set_view(self, view):
        self.__view__ = view
        self.__controls_controller__.set_view(view.get_controls_view())
        self.__connection_controller__.set_view(view.get_connection_view())
        self.__messages_controller__.set_view(view.get_messages_view())
        self.__screen_controller__.set_view(view.get_screen_view())
