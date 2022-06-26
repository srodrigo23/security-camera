from multiprocessing import Process, Queue
from threading import Thread
from util.logger import print_log

import sys
import cv2
import time

if sys.version_info >= (3, 0):
    from queue import Queue
else:
    from Queue import Queue

class WebCamera():
    
    def __init__(self, src, interface):
        """
        Constructor to webcamera with resolution
        """
        self.__src__ = src
        self.__interface__ = interface
        self.__frame__ = None
        self.__stopped__ = False
            
    def start(self): 
        """
        Method to init thread webcamera
        """
        self.__thread__ = Thread(target=self.catch_frames, args =())
        self.__thread__.daemon=True
        self.__thread__.start()
        
    def catch_frames(self):
        """
        Method to catch frames in 2 ways
        """
        self.__feed__ = cv2.VideoCapture(self.__src__)
        # self.__fps__ = int(self.__feed__.get(cv2.CAP_PROP_FPS))
        if self.__src__ == 0 : time.sleep(2.0)  # to charge the camera
        
        while not self.__stopped__:
            __ret__, __frame__ = self.__feed__.read()
            if __ret__:
                # time.sleep(1/self.__fps__)
                self.__frame__ = cv2.cvtColor(__frame__, cv2.COLOR_BGR2RGB)
            else:
                self.__interface__.stop()
        self.close()
    
    def get_frame(self):
        """
        Method to return a frame from webcam queue
        """
        return self.__frame__
    
    def is_more(self):
        """
        Method not used
        """
        return self.__frames_queue__.qsize() > 0

    def stop(self):
        """
        Method to stop catch frames
        """
        self.__stopped__ = True
    
    def close(self):
        self.__feed__.release()
        print_log('i', 'Finished capture frame')