
from node import Node
from settings import Settings
from connection import Connection

import sys
def run_node(params):
    """
    Start node in diferents modes depends promt params
    """
    settings = Settings()
    node = Node(params, settings)
    node.execute()
    
    connection = Connection(settings.get_host_address(
    ), settings.get_port(), settings.get_jpg_quality(), node)
    connection.execute()
    
# /Users/sergiorodrigo/Documents/tesis/code/videos/video1.mp4
"""
    python main.py cam    'path/to/the/video'
    python main.py cam    0
    python main.py picam  
"""
if __name__ == "__main__":
    run_node(sys.argv)
