from threading import Thread
import sys, cv2, time

if sys.version_info >= (3, 0):
    from queue import Queue
else:
    from Queue import Queue

class WebCamera():
    
    def __init__(self, src):
        self.source = cv2.VideoCapture(src)
        self.stopped = False
        self.frames_queue = Queue(maxsize=128)
    
    def start(self):
        self.thread = Thread(target=self.update, args=())
        self.thread.setDaemon(True)
        self.thread.start()
    
    def update(self):
        # time.sleep(2.0)
        while self.source.isOpened():
            if self.stopped:
                return
            else:
                grabbed, frame = self.source.read()
                if grabbed:
                    self.frames_queue.put(frame)

    def read(self):
        return self.frames_queue.get()
    
    def is_more(self):
        return self.frames_queue.qsize() > 0

    def stop(self):
        self.stopped = True