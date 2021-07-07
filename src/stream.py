import socket
import time

from comunication.image_sender import ImageSender
from node.camera_stream import CameraStream
from utils import resize

# import numpy as np


# this is better way without zmq sockets
# https://github.com/1010code/python-webcam-socket-streaming
# with this video
# https://www.youtube.com/watch?v=MQ8JfdvA7Yk
# https://www.youtube.com/watch?v=T0rYSFPAR0A
# https://gist.github.com/kittinan/e7ecefddda5616eab2765fdb2affed1b
# https://www.youtube.com/watch?v=7-O7yeO3hNQ

# Serialization socket
# https://pyzmq.readthedocs.io/en/latest/serialization.html
#
# 
# Server
# https://learning-0mq-with-pyzmq.readthedocs.io/en/latest/pyzmq/devices/streamer.html
# An excelent tool to deply the images throuht web 
# https://ngrok.com/docs
 


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
