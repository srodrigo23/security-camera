# read config file
from settings import Settings

class Camera:
    
    def __init__(self, mode):
        s = Settings()
        if mode == "CAM":
            from web_camera import WebCamera
            self.cam = WebCamera(src = s.get_source(), 
                                 resolution = s.get_resolution())
        elif mode == "PICAM":
            from pi_camera import PiCamera
            self.cam = PiCamera(resolution = s.get_resolution(), framerate=s.get_frame_rate())
        
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