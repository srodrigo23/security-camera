from threading import Thread
import sys
import cv2

if sys.version_info >= (3, 0):
    from queue import Queue
else:
    from Queue import Queue

class StreamWebCam():
    def __init__(self, 
                src, 
                queueSize=128):
        self.stream = cv2.VideoCapture(src)
        self.stopped = False
        self.my_queue = Queue(maxsize=queueSize)
    
    def start(self):
        t = Thread(target=self.update, args=())
        t.setDaemon(True)
        t.start()
        return self
    
    def update(self):
        while True:
            if self.stopped:
                return
            (grabbed, frame) = self.stream.read()
            self.my_queue.put(frame)

    def read(self):
        return self.my_queue.get()
    
    def is_more(self):
        return self.my_queue.qsize() > 0

    def stop(self):
        self.stopped = True

    