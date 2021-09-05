import sys
import cv2
import time
import utils
import imutils as im

from threading import Thread
from utils import resize
from loger import print_log

if sys.version_info >= (3, 0):
    from queue import Queue
else:
    from Queue import Queue
    
class WebCamera():
    
    def __init__(self, src, resolution):
        self.src = src
        self.resolution = resolution # to remove
        self.frames_queue = Queue(maxsize=64)
        self.ready = False
            
    def start(self):
        self.thread = Thread(target=self.catch_frames, args=())
        self.thread.setDaemon(True)
        self.thread.start()
    
    def set_source(self):
        self.feed = cv2.VideoCapture(self.src)
        self.ready = True
    
    def catch_frames(self):
        while True:
            self.set_source()
            if self.src=='0':
                time.sleep(2.0) # to charge the camera
            while self.ready:
                ret, frame = self.feed.read()
                if ret:
                    frame = im.resize(frame, self.resolution[0], self.resolution[1])
                    self.frames_queue.put(frame)
                else:
                    self.ready = False
    
    def read(self):
        return self.frames_queue.get()# if self.frames_queue.qsize() > 0 else None
    
    def is_more(self):
        return self.frames_queue.qsize() > 0

    def stop(self):
        self.feed.release()
        self.ready = False
        print_log('i', 'Finished capture frame')
