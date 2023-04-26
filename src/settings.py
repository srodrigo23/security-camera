# from configparser import ConfigParser

# parser = ConfigParser()
# parser.read('../config.ini')
import uuid


def get_host():
    """
    Method to return host from config.ini
    """
    return "127.0.0.1"
    # return parser.get('connection', 'host')
    
def get_port():
    """
    Method to return port from config.ini
    """
    return "49152"
    # return parser.get('connection', 'port')

def get_cam_id():
    """
    Method to return id camera from config.ini
    """
    code = str(uuid.uuid4().hex)
    return code[0:(len(code)//2)]
    # return parser.get('connection', 'cam_id')
