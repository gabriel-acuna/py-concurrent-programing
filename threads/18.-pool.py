import time
import logging
import threading
import random

from concurrent.futures import ThreadPoolExecutor

logging.basicConfig(level=logging.DEBUG, format='%(threadName)s => %(message)s',)

def math_operation(number1, number2):
    time.sleep(1)

    result = number1 + number2
    logging.info(f'Resultado de {number1} + {number2} = {result}')

if __name__ == '__main__':
    # for _ in range(0, 1000):
    #     thread = threading.Thread(target=math_operation, args=(random.randint(1,100),random.randint(1,100),))
    #     thread.start()
   
  
    with ThreadPoolExecutor(max_workers=10) as executor:
        for _ in range(0, 100):
            executor.submit(math_operation, random.randint(0,10),random.randint(0,10))
        executor.shutdown()
    
    logging.info(f'{time.perf_counter()} seconds process time')