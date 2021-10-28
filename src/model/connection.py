from threading import Thread
# from model.logger import print_log

import socket
import time
import struct
import pickle
import cv2

class Connection():
    
    def __init__(self, camera):
        """
        Constructor to connection
        """
        self.__camera__ = camera
        self.__socket_connected__ = None
        
    def set_socket_connected(self, socket):
        self.__socket_connected__ = socket
        
    def run_send_frames(self):
        """
        Method to prepare and execute connection, running a thread
        """
        if self.is_connectted():
            __connection__ = Thread(target=self.send_frames, args=())
            __connection__.daemon = True
            __connection__.start()
            
    def send_frames(self):
        """
        Method to send frames while the message is live
        """        
        while self.is_connectted():
            self.send_frame(self.__camera__.get_frame())
               
    def send_frame(self, frame):
        """
        Method to sent a frame throught socket connection
        """
        # pickle representation of the object obj as a bytes object, instead of writting it to a file
        encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), quality]
        result, image = cv2.imencode('.jpg', frame, encode_param)
        data = pickle.dumps(image, 0)
        self.__socket_connected__.sendall(struct.pack(">L", len(data)) + data)
        
    def is_connected(self):
        """
        Check if this node is connected
        """
        return not self.__socket_connected__ is None