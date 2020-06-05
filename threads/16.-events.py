import logging
import threading
import time

logging.basicConfig(level=logging.DEBUG, format='%(threadName)s => %(message)s')

def task1(event):
    logging.info('Waiting the event setting')
    event.wait()
    logging.info('Task 1')

def task2(event):
    while not  event.is_set():
        logging.info('Waiting the event setting')
        time.sleep(1)
    else:
        logging.info('Task 2')


if __name__ == '__main__':
    event = threading.Event()

    t1 = threading.Thread(target=task1, args=(event,))
    t2 = threading.Thread(target=task2, args=(event,))

    t1.start()
    t2.start()
    time.sleep(3)
    event.set()