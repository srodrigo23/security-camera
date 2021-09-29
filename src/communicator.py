from settings import Settings
from threading import Thread
from loger import print_log

import socket
import cv2
import time
import struct
import pickle

class Communicator():
    
    def __init__(self, settings):
        """
        """
        self.settings = settings
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = self.settings.get_host_address()
        self.port = self.settings.get_port()
        self.encode_param = [int(cv2.IMWRITE_JPEG_QUALITY),
                        self.settings.get_jpg_quality()]
    
    def init_connection(self):
        """
        """
        try:
            self.socket.connect((self.host, self.port))
        except socket.error as e:
            print_log('e', f'Connection don\'t reached {str(e)}')
        
    def send_frame(self, frame):
        """
        """
        # pickle representation of the object obj as a bytes object, instead of writting it to a file
        result, image = cv2.imencode('.jpg', frame, self.encode_param)
        data = pickle.dumps(image, 0)
        print(len(data))
        self.socket.sendall(struct.pack(">L", len(data)) + data)
