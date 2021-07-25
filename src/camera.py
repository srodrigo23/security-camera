class Camera:
    
    def __init__(self, src=0, use_pi_camera=False, resolution=(320, 240), frame_rate=32):
        if use_pi_camera:
            from pi_camera import PiCamera
            self.cam = PiCamera(resolution=resolution,
                                        framerate=frame_rate)
        else:
            from web_camera import WebCamera
            self.cam = WebCamera(src=src)
    
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