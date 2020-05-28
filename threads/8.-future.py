import time
import logging
import threading

from concurrent.futures import Future

logging.basicConfig(level=logging.DEBUG, format='%(message)s')

def future_callback(future):
    logging.info('Hallo, ich bin ein Callback, der ausgeführt wird, wenn die Zukunft einen Wert hat')
    logging.info(f'Der Zukunft ist: {future.result()}')


if __name__ == '__main__':
    future = Future()
    future.add_done_callback(future_callback)
    future.add_done_callback(
        lambda future: logging.info('Hallo, ich bin einen lambda!')
    )
    logging.info('Wir beginnen eine komplexe Aufgabe')
    time.sleep(2)
    logging.info('Wir haben die komplexe Aufgabe erledigt')
    logging.info('Wir werden der Zukunft einen Wert zuweisen')
    future.set_result('Die Nacht ist wunderschön')
    logging.info('Die Zukunft hat bereits Wert')