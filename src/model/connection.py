from threading import Thread
from util.logger import print_log

import socket
import time
import struct
import pickle
import cv2

class Connection():
    
    def __init__(self, camera, messages):
        """
        Constructor to connection
        """
        self.__camera__ = camera
        self.__socket_connected__ = None
        self.__messages_controller__ = messages
        
    def set_socket_connected(self, socket):
        """
        Set socket after get connection 
        """
        self.__socket_connected__ = socket
        
    def run_send_frames(self):
        """
        Method to prepare and execute connection, running a thread
        """
        if self.is_connected():
            __connection__ = Thread(target=self.send_frames, args=())
            __connection__.daemon = True
            __connection__.start()
            
    def send_frames(self):
        """
        Method to send frames while the message is live
        """        
        while self.is_connected() and not self.__camera__.is_none():
            time.sleep(0.1)
            frame = self.__camera__.get_frame()
            if not frame is None:
                self.send_frame(frame, 90)
        self.__messages_controller__.show_message_control('Transmission Terminated')
        print_log('i', "Frame Sent")
        
    def send_frame(self, frame, quality):
        """
        Method to sent a frame throught socket connection
        """
        # pickle representation of the object obj as a bytes object, instead of writting it to a file
        encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), quality]
        result, image = cv2.imencode('.jpg', frame, encode_param)
        data = pickle.dumps(image, 0)
        if self.is_connected():
            self.__socket_connected__.sendall(struct.pack(">L", len(data)) + data) # envio del frame
            self.__messages_controller__.show_message_control(
                Frame Sent')
            print_log('i', "Frame Sent")
        
        
    def is_connected(self):
        """
        Check if this node is connected
        """
        return not self.__socket_connected__ is None
    
    def check_camera_is_ready(self):
        return not self.__camera__.is_none()
