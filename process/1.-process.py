import time
import multiprocessing
import logging


logging.basicConfig(level=logging.DEBUG, format='%(process)s %(processName)s %(message)s')

def new_process(msg):
    ''' jj'''
    logging.info('Hi, I\'m a new process')
    time.sleep(10)
    logging.info(msg)
    logging.info('Process end')


if __name__ == '__main__':
    process = multiprocessing.Process(target=new_process, args=('Hi XD',), )
    process.start()
    process.join()
    logging.info('I\'m the parent process')
