import pickle
import socket
import struct
import time
from threading import Thread

import cv2
from util.logger import print_log


class Connection():
    
    def __init__(self, camera, messages):
        """ Constructor to connection object. """
        self.__camera__ = camera
        self.__socket_connected__ = None
        self.__messages_controller__ = messages
        self.__frames_counter__ = 0
        
    def set_socket_connected(self, socket):
        """ Set socket after get connection """
        self.__socket_connected__ = socket
    
    def set_camera_id(self, cam_id):
        """ Set camera id """
        self.__cam_id__ = cam_id
        
    def run_send_frames(self):
        """ Method to prepare and execute connection, running a thread. """
        if self.is_connected():
            __connection__ = Thread(target=self.send_frames, args=())
            __connection__.daemon = True
            __connection__.start()
    
    def set_controller_connection(self, controller):
        """ Method to interacts to the controller """
        self.__controller__ = controller
            
    def send_frames(self):
        """ Method to send frames while the message is live. """
        self.send_camera_id() #sending id camera
        while self.is_connected() and not self.__camera__.is_none():
            time.sleep(0.1)
            frame = self.__camera__.get_frame()
            if frame is not None:
                self.send_frame(frame, 90)
                self.__frames_counter__ += 1
                print_log('i', f"Frame Sent {self.__frames_counter__}")
        self.__frames_counter__ = 0
        
       
        self.__messages_controller__.show_message_control('Transmission Terminated')
        print_log('i', "Transmission Terminated")
        
    def send_frame(self, frame, quality):
        """ Method to sent a frame throught socket connection """
        # pickle representation of the object obj as a bytes object, instead of writting it to a file
        encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), quality]
        result, image = cv2.imencode('.jpg', frame, encode_param)
        data = pickle.dumps(image, 0)
        if self.is_connected():
            try:
                self.__socket_connected__.sendall(struct.pack(
                    ">L", len(data)) + data)  # envio del frame
            except socket.error:
                message = self.receive_message_connection_rejected()
                self.__controller__.disconnect_to_server()
                print_log('i', message)
                print_log('i', "Connection interrupted")
                self.__messages_controller__.show_message_control(message)
                self.__messages_controller__.show_message_control("Connection interrupted")
            else:
                self.__messages_controller__.show_message_control(
                    f'Frame Sent {self.__frames_counter__}')
    
    def receive_message_connection_rejected(self):
        try:
            message = self.__socket_connected__.recv(1024)
        except socket.error:
            message = "Server Outline..."
        return message

    def send_camera_id(self):
        """ Method to send an Id like a string. """
        self.__socket_connected__.send(self.__cam_id__.encode())
        
    def is_connected(self):
        """ Check if this node is connected. """
        return self.__socket_connected__ is not None
    
    def check_camera_is_ready(self):
        """ Method to check is the camera not is None to get frames is not ready. """
        return not self.__camera__.is_none()
