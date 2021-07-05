
class CameraStream:    
    def __init__(self, 
                 src=0, 
                 usePiCamera=False, 
                 resolution=(320, 240), 
                 framerate=32):
        if usePiCamera:
            from .picam_stream import PiCameraStream
            self.stream = PiCameraStream(resolution=resolution,
                                        framerate=framerate)
        else:
            from .webcam_stream import WebCamStream
            self.stream = WebCamStream(src=src)
    
    def start(self):
        return self.stream.start()
    
    def update(self):
        self.stream.update()
    
    def read(self):
        return self.stream.read()
    
    def stop(self):
        self.stream.stop()