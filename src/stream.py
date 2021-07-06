import socket
import time
# import numpy as np

from node.camera_stream import CameraStream
from comunication.image_sender import ImageSender
from utils import resize

tcp = 'tcp://192.168.100.8:5555'

def stream(tcp):
    sender = ImageSender(connect_to=tcp)
    #send node hostname wiht each image
    node_name = socket.gethostname() 
    node_cam = CameraStream(usePiCamera=False)
    node_cam.start()
    time.sleep(2.0) # allow camera sensor to warm up
    i = 0
    while True:
        image = node_cam.read()
        image = resize(image, width=320) #resize image
        # image = np.dstack([image, image, image]) # dont work's
        sender.send_image(node_name, image)
        print(f"Frame sent : {i}")
        i=i+1
stream(tcp)