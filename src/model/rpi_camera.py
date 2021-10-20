
from picamera.array import PiRGBArray
from picamera import PiCamera

from threading import Thread

class RPiCamera():
    
    def __init__(self, resolution, framerate):
        """
            Constructor to picamera with resolution and framerate by default
        """
        self.__camera__ = PiCamera()
        self.__camera__.resolution = resolution
        self.__camera__.framerate = framerate
        self.__raw_capture__ = PiRGBArray(self.__camera__, size=resolution)
        self.__stream__ = self.__camera__.capture_continuous(
            self.raw_capture, 
            format="bgr", 
            use_video_port=True)
        self.__frame__ = None
        self.__stopped__ = False
    
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
        for f in self.__stream__:
            self.__frame__ = f.array
            self.__raw_capture__.truncate(0)
            if self.__stopped__:
                self.close()
                return
                       
    def get_frame(self):
        """
        Method to get frame
        """
        return self.__frame__
    
    def stop(self):
        """
        Method to stop stream
        """
        self.__working__ = True
    
    def close(self):
        """
        Method to close stream object, raw capture and camera
        """
        self.__stream__.close()
        self.__raw_capture__.close()
        self.__camera__.close()
