import socket
import time

from node.camera_stream import CameraStream
from comunication.image_sender import ImageSender

tcp = 'tcp://192.168.43.98:5555'

def stream(tcp):
    sender = ImageSender(connect_to=tcp)
    #send node hostname wiht each image
    node_name = socket.gethostname() 
    node_cam = CameraStream(usePiCamera=False)
    node_cam.start()
    time.sleep(2.0) # allow camera sensor to warm up
    while True:
        image = node_cam.read()
        sender.send_image(node_name, image)
        
stream(tcp)