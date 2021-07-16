from picamera.array import PiRGBArray
from picamera import PiCamera

from threading import Thread
import cv2

class StreamPiCamera():
    
    def __init__(self, 
                 resolution=(320, 240), 
                 framerate=32):
        #initialize the camera and stream
        self.camera=PiCamera()
        self.camera.resolution=resolution
        self.camera.framerate=framerate
        self.rawCapture=PiRGBArray(self.camera, size=resolution)
        self.stream = self.camera.capture_continuous(self.rawCapture,
                                                     format="bgr", use_video_port=True)
        self.frame=None
        self.stopped=False
    
    def start(self):
        t = Thread(target=self.update, args=())
        t.setDaemon(True)
        t.start()
        return self
    
    def update(self):
        for f in self.stream:
            self.frame = f.array
            self.rawCapture.truncate(0)
            
            if self.stopped():
                close()
                return
                       
    def read(self):
        return self.frame
    
    def stop(self):
        self.stopped=True
    
    def close(self):
        self.stream.close()
        self.rawCapture.close()
        self.camera.close()
    