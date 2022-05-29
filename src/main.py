from view.monitor import Monitor
from controller.controller import Controller
from util.logger import print_log

def run_camera():
    """ Start node with command and gui interface """
    print_log('i', "Welcome to the camera simulator")
    __controller__ = Controller()
    __monitor__ = Monitor(__controller__)
    __controller__.set_view(__monitor__)
    __monitor__.mainloop()
        
if __name__ == "__main__":
    run_camera()