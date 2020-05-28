import logging

# Debug (10), Info (20), Warning (30), Error (40), Critical (50)

logging.basicConfig(
    level=logging.DEBUG,
    format='%(filename)s -- %(message)s -- %(levelname)s -- Thread: %(thread)s -- %(asctime)s',
    datefmt='%A %d-%m-%Y %H:%M:%S'
    #filename='logs/messages.txt'
    
    )

def messages():
    logging.debug('Debug message')
    logging.info('Info message')
    logging.warning('Warning message')
    logging.error('Error message')
    logging.critical('Critical message')


if __name__ == '__main__':
    messages()