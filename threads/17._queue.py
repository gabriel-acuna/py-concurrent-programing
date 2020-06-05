import queue
import logging
import threading
import time

logging.basicConfig(level=logging.DEBUG, format='%(threadName)s => %(message)s')

def show_elements():
    while not q.empty():
        item = q.get()
        logging.info(f'The element is {item}')
        q.task_done()
        time.sleep(0.5)

if __name__ == '__main__':
    q = queue.Queue()

    for val in range(1,21):
        q.put(val)
    
    logging.info('Queue already has elements')
    for _ in range (4):
        t = threading.Thread(target=show_elements)
        t.start()