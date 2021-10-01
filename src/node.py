from loger import print_log
from camera import Camera
from loger import print_log
from detector import MotionDetector
from connection import Connection

import time
import cv2
import datetime

class Node():
    
    def __init__(self, params, settings):
        """
        Constructor to init node picamera or webcamera
        """
        self.camera = Camera(mode=params[1], 
                             src=(params[2] if len(params) > 2 else None), 
                             settings=settings)
        self.ready = True
        self.camera.start()
            
    def execute(self):
        """
        Method to send frames when there is a flag to do it
        """
        print_log('i', 'Welcome node Camera...')
        while self.ready:
            try:
                time.sleep(1)
                # frame = self.camera.get_frame()
                # frame = self.draw_text(
                #     frame, message=f"Status: MOVEMENT", pos=(5, 13), color=(0, 0, 255))
                # self.connection.send_frame(frame)
            except KeyboardInterrupt:
                print_log('e', 'Node interrupted...')
                self.stop_node()
                         
    def stop_node(self):
        """
        Method to stop camera
        """
        self.ready = False
        self.camera.stop()
        # self.connection.close_connection()
        
    def draw_text(self, frame, message, pos, color):
        return cv2.putText(frame, message, pos,
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 1)
    
    # def add_labels(self, mov, frame):
    #     if mov:
    #         frame = self.draw_text(frame, 
    #                                message=f"Status: MOVEMENT", 
    #                                pos=(5, 13), 
    #                                color=(0, 0, 255))
    #     frame = self.draw_text(frame, message=datetime.datetime.now().strftime(
    #         "%A %d %B %Y %I:%M:%S%p"), pos=(5, frame.shape[0] - 5), color=(0, 0, 255))
    #     return frame
    # self.communicator.send_frame(frame)
        # mov, frame = self.motion_detector.detect_motion(frame)
        # frame = self.add_labels(mov, frame)
        # cv2.imshow('test', frame)
        # time.sleep(0.03)  # to prevent cpu overload
        # if cv2.waitKey(1) & 0xFF == ord('q'): break
