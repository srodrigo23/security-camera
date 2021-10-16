from model.socket import Socket

class SocketController():
    
    def __init__(self):
        self.__socket__ = Socket()
        print('socket importing')