class MessagesController():
    """ Messages Controller class to show messages in a list on the screen """
    def __init__(self):
        """ MVC pattern with view empty """
        self.__view__ = None
        
    def set_view(self, view):
        """ Set view to show messages on the screen """
        self.__messages_view__ = view    
    
    def show_message_control(self, message):
        """ Show on the screen messages on the screen with this controller """
        self.__messages_view__.add_message(message)