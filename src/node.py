import time
import cv2
import datetime

from settings import Settings
from loger import print_log
from camera import Camera
from loger import print_log
from detector import MotionDetector

"""
    python main.py CAM    'path/to/the/video'
    python main.py CAM    0
    python main.py PICAM  
"""

class Node():
    
    def __init__(self, params):
        self.settings = Settings()
        self.camera = self.create_camera(params)
        self.motion_detector = MotionDetector()
        self.ready = False

    def create_camera(self, params):
        return Camera(mode=params[1], 
                      src=(params[2] if len(params) > 2 else None), 
                      settings=self.settings)
    
    def show_captures(self):
        frame = self.camera.get_frame()
        mov, frame = self.motion_detector.detect_motion(frame)        
        if mov:
            frame = self.draw_text(frame, message=f"Status: MOVEMENT", pos=(5, 13), color=(0, 0, 255))
        frame = self.draw_text(frame, message=datetime.datetime.now().strftime(
            "%A %d %B %Y %I:%M:%S%p"), pos=(5, frame.shape[0] - 5), color=(0, 0, 255))
        cv2.imshow('test', frame)
    
    def run(self):
        print_log('i', 'Welcome node Camera...')
        try:
            while self.ready:
                self.show_captures()
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
        except KeyboardInterrupt:  # close all threads
            print_log('e', 'Node interrupted...')
            self.stop_node()
        else:
            print_log('i', 'Node turned off, unplug connection...')
        
    def launch(self):
        self.ready = True
        self.camera.start()
        self.run()
        
    def stop_node(self):
        self.ready = False
        self.camera.stop()

    def draw_text(self, frame, message, pos, color):
        return cv2.putText(frame, message, pos,
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 1)