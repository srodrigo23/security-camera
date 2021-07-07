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

# this tutorial
# https://www.pyimagesearch.com/2019/04/15/live-video-streaming-over-network-with-opencv-and-imagezmq/

#zmq
# https://github.com/jeffbass/imagezmq

# streaimg
# https://www.youtube.com/watch?v=-2vPmYHMJTQ
# http://helloraspberrypi.blogspot.com/2015/05/python-socket-server-to-send-camera_12.html


# Human activity recognition
# https://github.com/devindatt/AIDD_HAR_Demo
# https://github.com/shuvamdas/human-activity-recognition
# https://www.pyimagesearch.com/2019/11/25/human-activity-recognition-with-opencv-and-deep-learning/

# some issues about streaming
# https://stackoverflow.com/questions/36503536/send-video-over-tcp-using-opencv-and-sockets-in-raspberry-pi
# https://stackoverflow.com/questions/51921631/how-to-send-and-receive-webcam-stream-using-tcp-sockets-in-python

# this is a very important page. where i test the real neural network to recognice human actions
# https://learnopencv.com/introduction-to-video-classification-and-human-activity-recognition/
# https://everislatam.medium.com/video-analysis-to-detect-suspicious-activity-based-on-deep-learning-2218e754cdae
# data sets : https://www.researchgate.net/post/Is-there-a-dataset-from-surveillance-cameras-in-retail-stores-or-malls

# fire detection
# https://github.com/robmarkcole/fire-detection-from-images
# https://towardsdatascience.com/early-fire-detection-system-using-deep-learning-and-opencv-6cb60260d54a
# https://www.kaggle.com/ritupande/fire-detection-from-cctv
# https://www.kaggle.com/ritupande/fire-and-smoke-detection-in-cctv-footage/notebook#Data-Preparation

# Stream protocols
# http://profesores.elo.utfsm.cl/~agv/elo323/2s13/projects/reports/Mu%C3%83%C2%B1ozGarcia/Conceptos.html