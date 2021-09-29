
from node import Node
from settings import Settings

import sys
def run_node(params):
    """
    Start node in diferents modes depends promt params
    """
    settings = Settings()
    node = Node(params, settings)
    node.execute()

# /Users/sergiorodrigo/Documents/tesis/code/videos/video1.mp4
"""
    python main.py cam    'path/to/the/video'
    python main.py cam    0
    python main.py picam  
"""
if __name__ == "__main__":
    run_node(sys.argv)
