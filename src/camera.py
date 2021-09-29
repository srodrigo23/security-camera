
class Camera:
    """
    Interface to manage webcam and picam
    """
    def __init__(self, mode, src, settings):
        """
        Construtor to create a cam
        """
        if mode == "cam":
            from web_camera import WebCamera
            self.cam = WebCamera(src = (0 if src=='0' else src), 
                                 frame_size = settings.get_frame_size())
        elif mode == "picam":
            from pi_camera import PiCamera
            self.cam = PiCamera(resolution = settings.get_resolution(), 
                                framerate = settings.get_frame_rate())
        
    def start(self):
        """
        Method to start camera
        """
        return self.cam.start()
    
    def update(self):
        """
        Method to update frame only in picamera
        """
        self.cam.update()
    
    def get_frame(self):
        """
        """
        return self.cam.read()
    
    def stop(self):
        """
        """
        self.cam.stop()
    
    def there_is_frames(self):
        """
        """
        return self.cam.is_more()