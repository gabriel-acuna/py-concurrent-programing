import logging
import multiprocessing
import random

from multiprocessing import Pool

logging.basicConfig(level=logging.DEBUG, format='%(processName)s => %(message)s')

def is_even(number):
    return number, number % 2 == 0

if __name__ == '__main__':
    with Pool (processes=2) as excutor:
        for _ in range(10):
            result =  excutor.apply_async(is_even, args= (random.randint(0,100000),))
            result.wait()
            logging.info(f'Is {result.get()[0]} an even number? {result.get()[1]}')
           
