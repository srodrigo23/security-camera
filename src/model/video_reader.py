import sys
import cv2
import time

from threading import Thread
from utils import resize

if sys.version_info >= (3, 0):
    from queue import Queue
else:
    from Queue import Queue

class VideoReader:

    def __init__(self, path_video):
    
        self.__path__ = path_video
        self.__frames__ = Queue(maxsize = 10)

    def start_reader(self):
        __thread__ = Thread(target=self.read_frames, args=(__frames__))
        __thread__.setDaemon(True).start()

    def read_frames(self, queue):
        while True:
            __cap__ = cv2.VideoCapture(self.__path__)
            while True:
                __ret__, __frame__ = __cap__.read()
                if __ret__:
                    __frame__ = resize(__frame__, width=320)
                    queue.put(__frame__)
                else:
                    break
                time.sleep(0.2)
            time.sleep(0.2)

    def update(self):
        while self.source.isOpened():
            if self.stopped:
                return
            else:
                grabbed, frame = self.source.read()
                if grabbed:
                    self.frames_queue.put(frame)
