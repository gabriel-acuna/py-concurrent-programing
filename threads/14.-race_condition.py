import logging
import threading

logging.basicConfig(level=logging.DEBUG,
                    format="%(threadName)s => %(message)s")

BALANCE = 0

lock = threading.Lock()

def deposit(amount=0):
    global BALANCE
    for n in range(0, 1000000):
        try:
            lock.acquire()
            BALANCE += amount
        finally:
            lock.release()


def withdraw(amount=0):
    global BALANCE
    for n in range(0, 1000000):
        with lock:
            BALANCE -= amount
        

if __name__ == '__main__':
    th1 = threading.Thread(target=deposit, args=[100])
    th2 = threading.Thread(target=withdraw, args=[20])

    th1.start()
    th2.start()
    th1.join()
    th2.join()

    logging.info(f'Your current balance is: {BALANCE}')


