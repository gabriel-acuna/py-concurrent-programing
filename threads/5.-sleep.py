import time
import logging
import threading

logging.basicConfig(
    level=logging.DEBUG,
    format=' Thread: %(thread)s - %(threadName)s -- %(message)s',
    )

def task():
     logging.info('Wir machen eine neue Aufgabe')
     time.sleep(5)
     logging.info('Aufgabe ausgeführt')

if __name__ == '__main__':
   thread = threading.Thread(target=task)
   thread.start()