from picamera.array import PiRGBArray
from picamera import PiCamera
from threading import Thread

class PiCamera():
    
    def __init__(self, resolution, framerate):
        """
            Constructor to picamera with resolution and framerate by default
        """
        self.__camera__ = PiCamera()
        self.__camera__.resolution = resolution
        self.camera.framerate = framerate
        self.raw_capture = PiRGBArray(self.camera, size=resolution)
        self.stream = self.camera.capture_continuous(
            self.raw_capture, 
            format="bgr", 
            use_video_port=True)
        self.frame = None
        self.stopped = False
    
    def start(self):
        """
        Method to init thread picamera
        """
        self.thread = Thread(target=self.update, args=())
        self.thread.setDaemon(True)
        self.thread.start()
        
    def update(self):
        """
        Method to update frame to stream
        """
        for f in self.stream:
            self.frame = f.array
            self.raw_capture.truncate(0)
            if self.stopped:
                self.close()
                return
                       
    def read(self):
        """
        Method to get frame
        """
        return self.frame
    
    def stop(self):
        """
        Method to stop stream
        """
        self.stopped = True
    
    def close(self):
        """
        Method to close stream object, raw capture and camera
        """
        self.stream.close()
        self.raw_capture.close()
        self.camera.close()