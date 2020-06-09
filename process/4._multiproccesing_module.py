import time
import logging
import multiprocessing

logging.basicConfig(level=logging.DEBUG, format='%(message)s')

if __name__ == '__main__':
    current_process = multiprocessing.current_process()
    logging.info(f'Current process: {current_process} -- {current_process.pid}')