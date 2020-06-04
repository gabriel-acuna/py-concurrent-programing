import logging
import requests
import threading

from concurrent.futures import Future

logging.basicConfig(level=logging.DEBUG, format='%(message)s')

def genereate_request(url):
    future= Future ()
    t = threading.Thread(
        target = (lambda: future.set_result(requests.get(url)))
    )
    t.start()
    return future

def show_pokemon_name(response):
    if response.status_code == 200:
        response_json = response.json()
        pokemon_name = response_json['forms'][0]['name']
        logging.info(f"Die pokémon name ist {pokemon_name}")

def main():
    future = genereate_request('https://pokeapi.co/api/v2/pokemon/10')
    future.add_done_callback(
        lambda: show_pokemon_name(future.result()))
    while not future.done():
        logging.info('Warten auf ein Ergebnis')
    else:
        logging.info('Wir haben das Programm beendet')
    

if __name__ == '__main__':
    main()