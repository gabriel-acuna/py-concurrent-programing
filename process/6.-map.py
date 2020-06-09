from multiprocessing import Pool
import logging
import time
import random

logging.basicConfig(level=logging.DEBUG, format='%(processName)s => %(message)s')

def is_even(number):
    time.sleep(2)
    return number, number % 2 == 0

def show_result(results):
    for result in results:
        logging.info(f'Is {result[0]} an even number? {result[1]}')

if __name__ == '__main__':
    with Pool(processes=2) as executor:
        numbers =  [ random.randint(1,100000)  for number in range(10)]
        results =  executor.map_async(is_even, numbers,callback=show_result)
        results.wait()
       