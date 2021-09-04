
class Camera:
    """
    Interface to manage webcam and picam
    """
    def __init__(self, mode, src, settings):
        if mode == "cam":
            from web_camera import WebCamera
            self.cam = WebCamera(src = (0 if src=='0' else src), 
                                 resolution = settings.get_resolution())
        elif mode == "picam":
            from pi_camera import PiCamera
            self.cam = PiCamera(resolution = settings.get_resolution(), 
                                framerate=settings.get_frame_rate())
        
    def start(self):
        return self.cam.start()
    
    def update(self):
        self.cam.update()
    
    def get_frame(self):
        return self.cam.read()
    
    def stop(self):
        self.cam.stop()
    
    def there_is_frames(self):
        return self.cam.is_more()