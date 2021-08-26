import settings import Settings
import socket
import cv2
import time
from encoder import encode

class SocketConnection():
    
    def __init__(self, camera):
        
        self.s = Settings()
        self.cam = camera
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = s.get_host_address()
        self.port = s.get_port()
    
        self.init_connection()
        self.start_send_frames()
    
    def init_connection(self):
        try:
            self.socket.connect((self.host, self.port))
        except socket.error as e:
            print(str(e))

    def star_send_frames(self):
        thread = Thread(target=self.run_send_frames, args=(,))
        thread.setDaemon(True)
        thread.start()
    
    def run_send_frames(self):
        img_counter = 0
        # time.sleep(1.0)
        while True:
            frame = cam.get_frame()
            data = encode(frame)
            if img_counter%10==0:
                self.socket.sendall(
                    struct.pack(">L", len(data)) + #tamanio del frame
                    data # el frame
                )
            img_counter += 1