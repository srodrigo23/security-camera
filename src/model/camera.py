
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
        """
        Set source from WebCamera or Laptop Camera, size=(320, 240)
        """
        from .web_camera import WebCamera
        self.__cam__ = WebCamera(src, self)
        
    def set_picam(self, resolution=(1920, 1080), framerate=30):
        """
        Set source from PiCamera
        """
        from .rpi_camera import RPiCamera
        self.__cam__ = RPiCamera(resolution, framerate)
        
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
        Return frame stored in a variable
        """
        if self.__cam__ is not None:
            return self.__cam__.get_frame()
        else:
            return None
    
    def stop(self):
        """
        Stop camera and close
        """
        self.__cam__.stop()
        self.__cam__ = None
    
    def get_status(self):
        return self.__cam__.get_status_working()
    
    def there_is_frames(self):
        """
        Return if there is more frames
        """
        return self.__cam__.is_more()
    
    def is_none(self):
        """
        Return True if there is no Camera instance
        """
        return self.__cam__ is None
