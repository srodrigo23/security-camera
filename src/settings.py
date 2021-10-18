from configparser import ConfigParser

class Settings():
    
    def __init__(self):
        self.__parser__ = ConfigParser()
        self.__parser__.read('../config.ini')
    
    def get_host(self):
        return self.__parser__.get('connection', 'host')
        
    def get_port(self):
        return self.__parser__.get('connection', 'port')
