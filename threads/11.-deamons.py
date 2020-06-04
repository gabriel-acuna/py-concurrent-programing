import time
import logging
import requests
import threading

logging.basicConfig(level=logging.DEBUG, format='%(message)s')

def thread():
    logging.info('Hi, I\'m a single thread')
    time.sleep(2)
    logging.info('The program ends when I finish')

def deamon_thread():
    while True:
        logging.info('I\'m running in background!')
        time.sleep(0.3)

if __name__ == '__main__':
    thread = threading.Thread(target=deamon_thread, daemon=True)
    thread.start()

    input('Press enter to finish the main thread ')
