from .web_camera import WebCamera

class Camera():
    
    """
    Interface to manage webcam and picam
    """
    def __init__(self):
        """
            Construtor to create an empty cam
        """
        self.__cam__ = None
    
    def set_webcam(self, src=0):
         
        self.__cam__ = WebCamera(src)
        
    def set_picam(self, resolution=(320, 240), framerate=32):
    
        self.__cam__ = PiCamera(resolution, framerate)
        
    def start(self):
        """
        Method to start camera
        """
        return self.__cam__.start()
    
    def update(self):
        """
        Method to update frame only in picamera
        """
        self.__cam__.update()
    
    def get_frame(self):
        """
        Return frame stored in a queue
        """
        return self.__cam__.read()
    
    def stop(self):
        """
        Stop camera and close
        """
        self.__cam__.stop()
    
    def there_is_frames(self):
        """
        Return if there is more frames
        """
        return self.__cam__.is_more()