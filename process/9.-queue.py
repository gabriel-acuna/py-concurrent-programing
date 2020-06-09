import  time
import logging
import multiprocessing

logging.basicConfig(level=logging.DEBUG, format='%(processName)s => %(message)s')

def get_elements(queue):
    while not queue.empty():
        element = queue.get(block=True)
        logging.info(f'element : {element}')

if __name__ == '__main__':
    manager = multiprocessing.Manager()
    queue = manager.Queue()

    for x in range(30):
        queue.put(x)
    
    logging.info('Queue has elements')

    p1 = multiprocessing.Process(target=get_elements, args=(queue,))
    p2 = multiprocessing.Process(target=get_elements, args=(queue,))
    p3 = multiprocessing.Process(target=get_elements, args=(queue,))

    p1.start()
    p2.start()
    p3.start()

    p1.join()
    p2.join()
    p3.join()
