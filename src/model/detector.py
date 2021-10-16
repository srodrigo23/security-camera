import cv2

class MotionDetector:
    
    def __init__(self):
        self.static_back = None
    
    def detect_motion(self, frame):
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur(gray, (21, 21), 0)
        if self.static_back is None:
            self.static_back = gray
            return (False, frame)
        else:
            cnts = self.check_diferences(gray)
            if len(cnts) > 0:
                return (True, self.draw_conts(frame, cnts))
            else:
                return (False, frame)
        
    def check_diferences(self, gray):
        diff_frame = cv2.absdiff(self.static_back, gray)
        thresh_frame = cv2.threshold(diff_frame, 25, 255, cv2.THRESH_BINARY)[1]
        thresh_frame = cv2.dilate(thresh_frame, None, iterations=3)
        cnts, _ = cv2.findContours(thresh_frame.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        return cnts
    
    def draw_conts(self, frame, conts):
        for contour in conts:
            if cv2.contourArea(contour) >= 1000:  # < menor que
                (x, y, w, h) = cv2.boundingRect(contour)
                cv2.rectangle(frame, (x, y), (x + w, y + h), (10, 255, 120), 1)
        return frame