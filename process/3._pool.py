import logging
from concurrent.futures import ProcessPoolExecutor
import random

logging.basicConfig(level=logging.DEBUG, format='%(processName)s => %(message)s')


def is_even(number):
    return number % 2 == 0

if __name__ == '__main__':
    with ProcessPoolExecutor(max_workers=2) as executor:
        for _ in range(10):
            future =  executor.submit(is_even, random.randint(0,100000))
            future.add_done_callback(
                lambda future : logging.info(f'Is an even number? {future.result()}')
            )


