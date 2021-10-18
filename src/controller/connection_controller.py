from model.socket import Socket

class ConnectionController():
    
    def __init__(self):
        self.__view__ = None
        
        self.__socket__ = Socket() #TODO experimental
        self.connected = False # experimental
    
    def set_view(self, view):
        self.__connection_view__ = view
    
    def connect_to_server(self):
        if self.connected:
            self.__connection_view__.set_label_btn_connect('Connect')
            self.__connection_view__.enable_ent_ip()
            self.__connection_view__.enable_ent_port()
            
            # to disconnect to the server
            
            self.connected = False
        else:
            ip, port = self.__connection_view__.get_connection_info()
            if self.validate_ip_address(ip) and self.validate_port(port):
                self.__connection_view__.set_label_btn_connect('Disconnect')
                self.__connection_view__.disable_ent_ip()
                self.__connection_view__.disable_ent_port()
                self.connected = True
                
                # to connecto to the server
                
            else:
                self.__connection_view__.show_alert_message('Ip and Port error')

    def validate_ip_address(self, address):
        if not address is None:
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
        if not isinstance(int(port), int):
            return False
        else:
            return 1 <= int(port) <= 65535
