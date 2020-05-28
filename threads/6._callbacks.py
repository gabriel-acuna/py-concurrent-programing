import logging
import requests
import threading

logging.basicConfig(level=logging.DEBUG, format='%(message)s')


def get_pokemon_name(response_json):
    pokemon_name = response_json['forms'][0]['name']
    logging.info(f"Die pokémon name ist {pokemon_name}")

def get_random_name(response_json):
    random_name = response_json['results'][0]['name']['first']
    logging.info(f'Die person name ist {random_name}')

def error():
    logging.error('Operation konnte nicht abgeschlossen werden')


def generate_request(url, success_callback, error_callback):
    response = requests.get(url)
    if response.status_code == 200:
        success_callback(response.json())
    else:
        error_callback()


if __name__ == "__main__":
    thread1 = threading.Thread(target=generate_request, kwargs={
        'url': 'https://pokeapi.co/api/v2/pokemon/1',
        'success_callback': get_pokemon_name,
        'error_callback': error
    })
    thread1.start()

    thread2 = threading.Thread(target=generate_request, kwargs={
        'url': 'https://randomuser.me/api',
        'success_callback': get_random_name,
        'error_callback': error
    })
    thread2.start()