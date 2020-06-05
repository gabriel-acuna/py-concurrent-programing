import logging
import threading

logging.basicConfig(level=logging.DEBUG, format="%(threadName)s => %(message)s")

BALANCE = 100

lock = threading.RLock()

if __name__ == '__main__':
    lock.acquire()
    BALANCE -=30
    lock.release()

    logging.info(f'Your current balance is: {BALANCE}')