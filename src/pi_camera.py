from picamera.array import PiRGBArray
from picamera import PiCamera
from threading import Thread

class PiCamera():
    
    def __init__(self, resolution=(320, 240), framerate=32):
        self.camera = PiCamera()
        self.camera.resolution = resolution
        self.camera.framerate = framerate
        self.raw_capture = PiRGBArray(self.camera, size=resolution)
        self.stream = self.camera.capture_continuous(
            self.raw_capture, 
            format="bgr", 
            use_video_port=True)
        self.frame = None
        self.stopped = False
    
    def start(self):
        self.thread = Thread(target=self.update, args=())
        self.thread.setDaemon(True)
        self.thread.start()
        
    def update(self):
        for f in self.stream:
            self.frame = f.array
            self.raw_capture.truncate(0)
            if self.stopped():
                self.close()
                return
                       
    def read(self):
        return self.frame
    
    def stop(self):
        self.stopped = True
    
    def close(self):
        self.stream.close()
        self.raw_capture.close()
        self.camera.close()