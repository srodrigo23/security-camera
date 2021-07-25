import socket, time, numpy as np

from image_sender import ImageSender
from stream_camera import StreamCamera
from utils import resize

import cv2

tcp_ip = "127.0.0.1"
tcp_port = "5555"

tcp = 'tcp://'+ tcp_ip + ':' + tcp_port

def stream(tcp):
    sender = ImageSender(connect_to=tcp)
    node_name = socket.gethostname() 
    node_cam = StreamCamera(usePiCamera=False)
    node_cam.start()
    time.sleep(2.0) # allow camera sensor to warm up
    # i = 0
    while True:
        image = node_cam.read()
        # image = resize(image, width=320) #resize image
        image = np.dstack([image, image, image])
        cv.imshow('test', image)
        # sender.send_image(node_name, image)
        # print(f"Frame sent : {i}")
        # i=i+1
        
stream(tcp)