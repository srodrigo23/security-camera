import sys
import cv2
import time
import utils

from threading import Thread
from utils import resize
from loger import print_log

if sys.version_info >= (3, 0):
    from queue import Queue
else:
    from Queue import Queue
    
class WebCamera():
    
    def __init__(self, src, resolution):
        self.source = cv2.VideoCapture(src)
        self.resolution = resolution # to remove
        self.frames_queue = Queue(maxsize=128)
        self.ready = False
            
    def start(self):
        self.ready = True
        self.thread = Thread(target=self.update, args=())
        self.thread.setDaemon(True)
        self.thread.start()
    
    def update(self):
        if self.source == "0":
            time.sleep(2.0)  # to load camera
        while self.ready:
            ret, frame = self.source.read()
            if ret:
                self.frames_queue.put(frame)
                
    def read(self):
        return self.frames_queue.get()# if self.frames_queue.qsize() > 0 else None
    
    def is_more(self):
        return self.frames_queue.qsize() > 0

    def stop(self):
        self.source.release()
        self.ready = False
        print_log('i', 'Finished capture frame')
