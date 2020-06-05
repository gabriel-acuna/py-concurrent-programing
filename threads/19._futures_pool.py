import time
import logging
import requests
import threading

from concurrent.futures import as_completed
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import as_completed

logging.basicConfig(level=logging.DEBUG, format='%(threadName)s: %(message)s',)

URLS = [
    'https://codigofacilito.com/',
    'https://twitter.com/home',
    'https://www.google.com/',
    'https://es.stackoverflow.com/',
    'https://stackoverflow.com/',
    'https://about.gitlab.com/',
    'https://github.com/',
    'https://www.youtube.com/'
]


def generate_request(url):
    return requests.get(url)

def check_status_code(response, url):
   
    logging.info(f'La respuesta del servidor {url} es: {response.status_code}')

def factorial(number):
    f = 1

    if number >= 0 and number < 2:
        return f

    for n in range(1, number+1):
        f = f * n
    return number, f



if __name__ == '__main__':
    with ThreadPoolExecutor(max_workers=2) as executor:

        # results = [executor.submit(generate_request, url) for url in URLS]
        results = executor.map(generate_request, URLS)

        for url, response in zip(URLS, results):
            if response.status_code == 200:
                check_status_code(response, url)
        
        f = executor.submit(factorial, 6)
        f.add_done_callback(
            lambda future : logging.info(f'El factorial de {future.result()[0]} es {future.result()[1]}')
        )
