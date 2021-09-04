from settings import Settings
from threading import Thread
from encoder import encode

import socket
import cv2
import time
import struct

from loger import print_log

class Comunicator():
    
    def __init__(self, settings):
        self.settings = settings
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = self.settings.get_host_address()
        self.port = self.settings.get_port()
    
    def init_connection(self):
        try:
            self.socket.connect((self.host, self.port))
        except socket.error as e:
            print_lig('e', f'Connection don\'t reached {str(e)}')
        
    def send_frame(self, frame):    
        data = encode(frame)
        self.socket.sendall(struct.pack(">L", len(data)) + data)

    def encode(self, frame):
        encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), self.settings.get_jpg_quality()]
        result, image = cv2.imencode('.jpg', frame, encode_param)
        if result:
            # pickle representation of the object obj as a bytes object, instead of writting it to a file
            return pickle.dumps(image, 0)
