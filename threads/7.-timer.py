import logging
import threading

logging.basicConfig(level=logging.DEBUG, format='%(message)s')

def callback():
    logging.info('Hallo, ich bin ein callback, der nicht sofort ausgeführt wird')

if __name__ == '__main__':
    thread = threading.Timer(3, callback)
    thread.start()

    logging.info('Hallo, ich bin im Hauptthread')
    logging.info('Wir warten auf die callback Ausführung')