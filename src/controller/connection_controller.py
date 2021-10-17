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
            self.connected = False
        else:
            self.__connection_view__.set_label_btn_connect('Disconnect')
            self.__connection_view__.disable_ent_ip()
            self.__connection_view__.disable_ent_port()
            self.connected = True

        
        
