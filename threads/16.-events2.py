import time
import logging
import requests
import threading

logging.basicConfig(level=logging.DEBUG, format='%(threadName)s => %(message)s')

user = {}

def generate_request(url,event):
    global user

    resp = requests.get(url)
    if resp.status_code == 200:
        response_json = resp.json()

        user = response_json.get('results')[0]
        event.set()
    
def show_user_name(event):
    event.wait()
    name = user.get('name').get('first')
    logging.info(f'The user\'s name is {name}')

if __name__ == '__main__':
    event = threading.Event()
    t1 = threading.Thread(target=generate_request, args=['https://randomuser.me/api', event])
    t2 = threading.Thread(target=show_user_name, args=[event])

    t1.start()
    t2.start()
    