import time
import logging
import threading

logging.basicConfig(level=logging.DEBUG, format='%(message)s')

def new_trask():
    current_thread = threading.current_thread()
    name = current_thread.getName()
    id = threading.get_ident()
    logging.info(f'Current thread is {name} and his id is {id}')


if __name__ == '__main__':
    thread = threading.Thread(target=new_trask, name='thread-test')
    thread.start()
    for t in threading.enumerate():
        if t == threading.main_thread():
            logging.info('We are in the main thread')
        logging.info(t)
