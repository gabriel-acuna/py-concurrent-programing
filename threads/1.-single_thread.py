import requests
import threading

def get_name():
    response = requests.get('https://randomuser.me/api')
    if response.status_code == 200:
        results = response.json().get('results')
        name = results[0].get('name').get('first')
        print(name)

if __name__ == '__main__':
    for _ in range(0,20):
        thread = threading.Thread(target=get_name)
        thread.start()