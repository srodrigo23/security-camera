

class MessagesController():
    
    def __init__(self):
        self.__view__ = None
        
    def set_view(self, view):
        self.__messages_view__ = view    
    
    def show_message_control(self, message):
        self.__messages_view__.add_message(message)