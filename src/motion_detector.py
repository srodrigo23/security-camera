import cv2, pandas, imutils
from utils import resize
import time

class MotionDetector:
    
    def __init__(self, camera):
        self.camera = camera
        self.static_back = None
        self.motion_list = [None, None] # List when any moving object appear
        self.time = [] #Time of movement
        self.df = pandas.DataFrame(
            columns=["Start", "End"]
        )
        self.stopped = False
    
    def start(self):
        self.thread = Thread(target=self.detect_motion, args=())
        self.thread.setDaemon(True)
        self.thread.start()
        
    def detect_motion(self):
        time.sleep(2.0)
        while True:
        # while self.camera.there_is_frames():
            frame = self.camera.get_frame()
            # print(type(frame))
            self.motion = False
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            gray = cv2.GaussianBlur(gray, (21, 21), 0)
            if self.static_back is None:
                self.static_back = gray
                continue
            
            diff_frame = cv2.absdiff(self.static_back, gray)
            thresh_frame = cv2.threshold(diff_frame, 30, 255, cv2.THRESH_BINARY)[1]
            thresh_frame = cv2.dilate(thresh_frame, None, iterations = 3)
            cnts,_ = cv2.findContours(thresh_frame.copy(),
                    cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            for contour in cnts:
                if cv2.contourArea(contour) < 1000:
                    continue
                self.motion = True

                (x, y, w, h) = cv2.boundingRect(contour)
                # making green rectangle arround the moving object
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 1)
                cv2.putText(frame, "Status: {}".format('Movement'), (20, 20), cv2.FONT_HERSHEY_SIMPLEX,
                    1, (0, 0, 255), 3)
            
            # frame = resize(frame, width=0) #resize image
            cv2.imshow("Diference", frame)
            
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        cv2.destroyAllWindows()