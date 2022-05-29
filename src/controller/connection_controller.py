import time
import socket as sckt

from _thread import start_new_thread
from util.logger import print_log

class ConnectionController():
    """ Connection Controller class to control view and conection with the server """
    def __init__(self, connection, messages_controller):
        """
        Init class t do the connection and show info on the screen
        """
        self.__connection_view__ = None
        self.__connection__ = connection
        self.__messages_controller__ = messages_controller
        self.__socket__ = None
        self.__connection__.set_controller_connection(self)
        
    def set_view(self, view):
        """ MVC pattern to set control view """
        self.__connection_view__ = view
        
    def disconnect_to_server(self):
        """ Method to set to none socket communication """
        self.__socket__ = None
        self.__connection__.set_socket_connected(self.__socket__)
        self.enable_controls()  # to disconnect to the server
    
    def connect_to_server(self):
        """ Method to connect to the server socket checking fields """
        if self.__connection__.check_camera_is_ready():  # only with video working
            if self.__connection__.is_connected():
                self.disconnect_to_server()
            else:
                __host__, __port__, __cam_id__ = self.__connection_view__.get_connection_info()
                if self.validate_host_address(__host__) and self.validate_port(__port__):
                    self.disable_controls()  # to connect to the server
                    self.__connection_view__.set_label_btn_connect('Connecting')
                    self.__connection_view__.disable_btn_connect()
                    start_new_thread(self.attempt_connect_to_socket, (__host__, __port__, __cam_id__, 5, 0.5)) #thread!!!
                else:
                    self.__connection_view__.show_alert_message('Ip and Port error')
        else:
            self.__connection_view__.show_alert_message("It can't transmit yet")
                                
    def attempt_connect_to_socket(self, host, port, cam_id ,num_attempts, time_delay):
        """ Method to live like a thread to attempt connect to the server. """
        cont = 0
        while self.__socket__ is None and cont < num_attempts:
            cont = cont + 1
            try:
                self.__socket__ = sckt.socket(sckt.AF_INET, sckt.SOCK_STREAM)
                time.sleep(time_delay)
                self.__socket__.connect((host, int(port)))
            except sckt.error as e:
                self.__messages_controller__.show_message_control(str(e))
                print_log('i', "Failed Connection")
                self.__socket__ = None
            else:
                #set socket to init to transmite images
                self.__messages_controller__.show_message_control("Connected to the server")
                print_log('i', "Connected to the server")
                
        if self.__socket__ is None:
            self.__messages_controller__.show_message_control("Failed Connection")
            self.enable_controls()
        else:
            self.disable_controls()
            self.__connection__.set_socket_connected(self.__socket__)
            self.__connection__.set_camera_id(cam_id)
            self.__connection__.run_send_frames() # start to send frames
            
    def enable_controls(self):
        """ Enable controls to fill ip and port to connect to the socket server. """
        self.__connection_view__.set_label_btn_connect('Connect')
        self.__connection_view__.enable_btn_connect()
        self.__connection_view__.enable_ent_ip()
        self.__connection_view__.enable_ent_port()
        self.__connection_view__.enable_ent_cam_id()
    
    def disable_controls(self):
        """ Disable controls after attempt to connect to the server socket. """
        self.__connection_view__.set_label_btn_connect('Stop Connection')
        self.__connection_view__.enable_btn_connect()
        self.__connection_view__.disable_ent_ip()
        self.__connection_view__.disable_ent_port()
        self.__connection_view__.disable_ent_cam_id()

    def validate_host_address(self, address):
        """ Method to test host to connect to the server. """
        if address is not None:
            __parts__ = address.split(".")    
            if len(__parts__) != 4:
                return False
            else:
                for __part__ in __parts__:
                    if not isinstance(int(__part__), int) and (int(__part__) < 0 or int(__part__) > 255):
                        return False
                return True
        else:
            return False

    def validate_port(self, port):
        """ Method to test port to connect to the server. """
        if not isinstance(int(port), int):
            return False
        else:
            return 1 <= int(port) <= 65535
