import sys
from node import Node

def run_node(params):
    node = Node(params)
    node.launch()

if __name__ == "__main__":
    run_node(sys.argv)