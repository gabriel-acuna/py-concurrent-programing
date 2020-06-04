from pymongo import MongoClient
import logging
import requests
import threading

logging.basicConfig(level=logging.DEBUG, format='%(message)s')


def lists_mongo_databases():
    client = MongoClient()
    databases = client.list_databases()
    logging.info('******  Databases *******')
    for db in databases:
        logging.info(f'\t * {db.get("name")}')
    logging.info('\n------------------------\n')
def get_github_profile(user):
    response = requests.get(f'https://api.github.com/users/{user}')
    if response.status_code == 200:
        logging.info(f'\nGithub User Info')
        user = response.json()
        for key in user:
            logging.info(f'\n{key}: {user.get(key)}')
   
    

def main():
    t1 = threading.Thread(target=lists_mongo_databases)
    t2 = threading.Thread(target=get_github_profile, kwargs={'user': 'gstef09'})


    t1.start()
    t2.start()
    t1.join()
    t2.join()

    logging.info('\nProgram ended,the threads have finished')

if __name__ == '__main__':
    main()

