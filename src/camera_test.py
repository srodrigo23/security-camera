import cv2
import imutils

class Camera(object):
    """
    Camera that return a frame
    """
    def __init__(self, src=0):
        self.video_capture = cv2.VideoCapture(src)
        
    def close_camera(self):
        self.video_capture.release()
    
    def get_frame(self):
        if self.video_capture.isOpened():
            ret, frame = self.video_capture.read()
            # frame = imutils.resize(frame, width=320)
            if ret:
                # return (ret, cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
                return(ret, frame)
            else:
                return (ret, None)
        else:
            return None