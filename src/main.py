from view.monitor import Monitor
from controller.controller import Controller
from settings import Settings


def run_camera():
    """
        Start node with command and gui interface
    """
    __settings__ = Settings()
    __controller__ = Controller()
    __monitor__ = Monitor(__controller__, __settings__)
    
    __controller__.set_view(__monitor__)    
    __monitor__.mainloop()
        
if __name__ == "__main__":
    run_camera()
