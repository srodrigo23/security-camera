from configparser import ConfigParser

class Settings():
    
    def __init__(self):
        """
        Settings object to parser Config file
        """
        self.__parser__ = ConfigParser()
        self.__parser__.read('../config.ini')
    
    def get_host(self):
        """
        Method to return host from config.ini
        """
        return self.__parser__.get('connection', 'host')
        
    def get_port(self):
        """
        Method to return port from config.ini
        """
        return self.__parser__.get('connection', 'port')
