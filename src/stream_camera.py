class StreamCamera:
    
    def __init__(self, src=0, usePiCamera=False, resolution=(320, 240), framerate=32):
        
        if usePiCamera:
            from stream_picam import StreamPiCamera
            self.stream = StreamPiCamera(resolution=resolution,
                                        framerate=framerate)
        else:
            from stream_webcam import StreamWebCam
            self.stream = StreamWebCam(src=src)
    
    def start(self):
        return self.stream.start()
    
    def update(self):
        self.stream.update()
    
    def read(self):
        return self.stream.read()
    
    def stop(self):
        self.stream.stop()