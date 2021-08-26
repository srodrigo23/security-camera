from settings import Settings
from threading import Thread
from encoder import encode

import socket
import cv2
import time
import struct


class SocketConnection():
    
    def __init__(self, camera):
        
        self.settings = Settings()
        self.cam = camera
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = self.settings.get_host_address()
        self.port = self.settings.get_port()
    
        self.init_connection()
        
    
    def init_connection(self):
        try:
            self.socket.connect((self.host, self.port))
        except socket.error as e:
            print(str(e))
        self.start_send_frames()

    def start_send_frames(self):
        thread = Thread(target=self.run_send_frames, args=())
        thread.setDaemon(True)
        thread.start()
    
    def run_send_frames(self):
        img_counter = 0
        # time.sleep(1.0)
        while True:
            frame = self.cam.get_frame()
            data = encode(frame)
            print(len(data))
            if img_counter%1==0:
                self.socket.sendall(
                    struct.pack(">L", len(data)) + data # el frame
                )
            img_counter += 1
