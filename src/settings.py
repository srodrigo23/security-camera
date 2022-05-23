from configparser import ConfigParser

parser = ConfigParser()
parser.read('../config.ini')

def get_host():
    """
    Method to return host from config.ini
    """
    return parser.get('connection', 'host')
    
def get_port():
    """
    Method to return port from config.ini
    """
    return parser.get('connection', 'port')

def get_cam_id():
    """
    Method to return id camera from config.ini
    """
    return parser.get('connection', 'cam_id')
