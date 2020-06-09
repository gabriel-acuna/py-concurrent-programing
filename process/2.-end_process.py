import os
import time
import logging
import multiprocessing


logging.basicConfig(level=logging.DEBUG, format='%(message)s')

def child_process():
    logging.info('Hi, I am a child process')
    time.sleep(6)
    logging.info('Process end')

if __name__ == '__main__':
    p = multiprocessing.Process(target=child_process)
    p.start()
    time.sleep(8)
    if p.is_alive(): 
        p.terminate()
        logging.info('Child process ended prematurely')
    logging.info('End of the program')