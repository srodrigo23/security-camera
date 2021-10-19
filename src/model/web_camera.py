from multiprocessing import Process, Queue 
from threading import Thread
from .loger import print_log

import sys
import cv2
import time

if sys.version_info >= (3, 0):
    from queue import Queue
else:
    from Queue import Queue
    
class WebCamera():
    
    def __init__(self, src, frame_size):
        """
            Constructor to webcamera with resolution
        """
        self.__src__ = src
        self.frame_size = frame_size
        self.__frames_queue__ = Queue(maxsize=64)
            
    def start(self): 
        """
            Method to init thread webcamera
        """
        self.thread = Thread(target=self.catch_frames, args =())
        self.thread.daemon=True
        self.thread.start()    
        
    def rescale_frame(self, frame, percent=75):
        """
            Method to resize a frame from original size about percent size
        """
        width = int(frame.shape[1] * percent / 100)
        height = int(frame.shape[0] * percent / 100)
        dim = (width, height)
        return cv2.resize(frame, dim, interpolation=cv2.INTER_AREA)
    
    def catch_frames(self):
        """
            Method to catch frames in 2 ways
        """
        self.feed = cv2.VideoCapture(src)
        # if self.src == '0' : time.sleep(2.0)  # to charge the camera
        while self.ready:
            time.sleep(self.time_sleep) 
            ret, frame = self.feed.read()
            if ret:
                frame = self.rescale_frame(frame, self.frame_size)
                self.frames_queue.put(frame)
            else:
                self.stop()
    
    def read(self):
        """
            Method to return a frame from webcam queue
        """
        return self.frames_queue.get()
    
    def is_more(self):
        """
            Method to know if there are more frames
        """
        return self.frames_queue.qsize() > 0

    def stop(self):
        """
            Method to stop catch frames
        """
        self.ready = False
        self.feed.release()
        print_log('i', 'Finished capture frame')
