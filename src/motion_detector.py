import cv2
import pandas
import time
import datetime
from utils import resize

class MotionDetector:
    
    def __init__(self, camera):
        self.camera = camera
        
        # self.motion_list = [None, None]
        # self.time = []
        # self.df = pandas.DataFrame(columns=["Start", "End"])
        # self.stopped = False
        
        self.message = ''
        self.frame = None
    
    def draw_contours(self, conts):
        for contour in conts:
            if cv2.contourArea(contour) < 1000:
                continue
            self.message = 'Movement'
            (x, y, w, h) = cv2.boundingRect(contour)
            # making green rectangle arround the moving object
            cv2.rectangle(self.frame, (x, y), (x + w, y + h), (10, 255, 120), 1)
    
    def draw_text(self, message, pos, color):
        cv2.putText(self.frame, message, pos, cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 1)
    
    def detect_motion(self, static_back, gray):
    
        diff_frame = cv2.absdiff(static_back, gray)
        thresh_frame = cv2.threshold(diff_frame, 25, 255, cv2.THRESH_BINARY)[1]
        thresh_frame = cv2.dilate(thresh_frame, None, iterations=3)
        cnts, _ = cv2.findContours(thresh_frame.copy(),
                                cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        return cnts
    
    def run(self):
        static_back = None
        while True:
            self.frame = self.camera.get_frame()
            self.message = 'Still'
            gray = cv2.cvtColor(self.frame, cv2.COLOR_BGR2GRAY)
            gray = cv2.GaussianBlur(gray, (21, 21), 0)
            
            if static_back is None:
                static_back = gray
                continue
            
            self.draw_contours(self.detect_motion(static_back=static_back, gray=gray))
            
            self.draw_text(message=f"Status: {self.message}", pos=(5, 13), color=(0, 0, 255))
            self.draw_text(message=datetime.datetime.now().strftime(
                "%A %d %B %Y %I:%M:%S%p"), pos=(5, self.frame.shape[0] - 5), color=(0, 0, 255))
                
            cv2.imshow("Diference", self.frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            
        cv2.destroyAllWindows()
