import  time
import random
import logging
import multiprocessing

logging.basicConfig(level=logging.DEBUG, format='%(processName)s => %(message)s')

def set_value(namespace):
    time.sleep(3)
    namespace.pin = random.randint(100,999)

def get_value(namespace):
    while namespace.pin is None:
        time.sleep(0.5)
        logging.info('PIN has no value yet')
    else:
        logging.info(f'PIN: {namespace.pin}')

if __name__ == '__main__':
    manager = multiprocessing.Manager()
    namespace = manager.Namespace()
    namespace.pin = None

    p1 = multiprocessing.Process(target=get_value, args=(namespace,))
    p2 = multiprocessing.Process(target=set_value, args=(namespace,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()