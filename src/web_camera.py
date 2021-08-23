from threading import Thread
from utils import resize
import sys, cv2, time, utils

if sys.version_info >= (3, 0):
    from queue import Queue
else:
    from Queue import Queue

class WebCamera():
    
    def __init__(self, src, resolution):
        self.source = cv2.VideoCapture(src)
        self.resolution = resolution 
        self.stopped = False
        self.frames_queue = Queue(maxsize=128)
    
    # thread to capture frames
    def start(self):
        self.thread = Thread(target=self.update, args=())
        self.thread.setDaemon(True)
        self.thread.start()
    
    def update(self):
        time.sleep(2.0) # to load camera
        while self.source.isOpened():
            if self.stopped:
                return
            else:
                grabbed, frame = self.source.read()
                frame = resize(frame, width=self.resolution[0], height=self.resolution[1])
                if grabbed:
                    self.frames_queue.put(frame)

    def read(self):
        return self.frames_queue.get()
    
    def is_more(self):
        return self.frames_queue.qsize() > 0

    def stop(self):
        self.stopped = True