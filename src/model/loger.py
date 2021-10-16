import logging

logging.basicConfig(
    filename='system.log',
    format='%(process)d %(asctime)s %(levelname)s : %(message)s', 
    level=logging.DEBUG, 
    datefmt='%m/%d/%Y %I:%M:%S %p')

def print_log(level, message):
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
