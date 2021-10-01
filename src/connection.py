from threading import Thread
from _thread import start_new_thread
from loger import print_log

import socket
import time
import struct
import pickle
import cv2

class Connection():
    
    def __init__(self, host, port, quality, node):
        """
        Constructor to get 
        """
        self.host = host
        self.port = port
        self.quality = quality # bad smell
        self.node = node
    
    def execute(self):
        """
        Method to prepare and execute connection, running a thread
        """
        self.socket = None
        self.connected = False
        self.send_frame = False
        start_new_thread(self.connect_socket, ())
        
    def connect_socket(self):
        """
        Method to live like a thread to attempt connect to the server
        """
        while not self.connected:
            try:
                self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                self.socket.connect((self.host, self.port))
                time.sleep(2.0)
            except socket.error as e:
                print_log('e', f'Connection don\'t reached {str(e)}')
            else:
                self.connected = True
                start_new_thread(self.listen_messages, ())
    
    def listen_messages(self):
        """
        Method to live like a thread to listen messages and manage it by two conditions
        """
        while self.connect:
            message = self.socket.recv(1024)
            message = message.decode('utf-8')
            
            if message == 'send':
                self.send_frame = True
                start_new_thread(self.send_frames, ())
            elif message == 'stop':
                self.send_frame = False
                
    def send_frames(self):
        """
        Method to send frames while the message is live
        """        
        while self.send_frame:
            time.sleep(0.5)
            send_frame(self.node.camera.get_frame())
               
    def send_frame(self, frame):
        """
        Method to sent a frame throught socket connection
        """
        # pickle representation of the object obj as a bytes object, instead of writting it to a file
        encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), quality]
        result, image = cv2.imencode('.jpg', frame, encode_param)
        data = pickle.dumps(image, 0)
        self.socket.sendall(struct.pack(">L", len(data)) + data)
