import logging
from util.date import get_current_time_string

logging.basicConfig(
    filename='system.log',
    format='%(process)d %(asctime)s %(levelname)s : %(message)s', 
    level=logging.DEBUG, 
    datefmt='%m/%d/%Y %I:%M:%S %p')

def print_log(level, message):
    """
    Method to print messages from system
    """
    d = get_current_time_string()
    if level == 'd':  # debug
        logging.debug(message)
    elif level == 'i':  # info
        logging.info(message)
    elif level == 'w':  # warning
        logging.warning(message)
    elif level == 'e':  # error
        logging.error(message)
    elif level == 'c':  # critical
        logging.critical(message)
    print(d,':', message)
