import time
import logging
import threading

logging.basicConfig(level=logging.DEBUG, format='%(threadName)s => %(message)s')

class ThreadTest(threading.Thread):

    def __init__(self,deamon=False):
        threading.Thread.__init__(self, daemon=deamon)


    def run(self):
        while True:
            logging.info('We should put here all task that we want executing concurrently')
            time.sleep(1)

if __name__ == '__main__':
    thread = ThreadTest(deamon=True)
    thread.start()
    time.sleep(3)
    logging.info('Program end')

