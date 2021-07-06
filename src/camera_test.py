import numpy as np
import time
import cv2
from utils import resize
from node.camera_stream import CameraStream

stream = CameraStream(0).start()

time.sleep(1.0) # to prepare camera
#TODO: resize image
while True:
    frame = stream.read()    
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    frame = np.dstack([frame, frame, frame])
    frame = resize(frame, width=320) #resize image
    cv2.imshow("Frame", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
stream.stop()