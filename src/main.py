
# from node import Node
# from settings import Settings
# from connection import Connection
from view.monitor import Monitor
from controller.controller import Controller

import sys

def __run_node__():
    """
        Start node with command and gui interface
    """
    __controller__ = Controller()
    __monitor__ = Monitor(__controller__)
    
    __controller__.set_view(__monitor__)    
    __monitor__.mainloop()

    # settings = Settings()
    # node = Node(params, settings)
    # connection = Connection(settings.get_host_address(
    # ), settings.get_port(), settings.get_jpg_quality(), node)
    # connection.execute()
    # node.execute()
        
# /Users/sergiorodrigo/Documents/tesis/code/videos/video1.mp4
if __name__ == "__main__":
    __run_node__()
