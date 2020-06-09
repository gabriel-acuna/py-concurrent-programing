import  time
import random
import logging
import multiprocessing

logging.basicConfig(level=logging.DEBUG, format='%(processName)s => %(message)s')

class Publisher(multiprocessing.Process):
    def __init__(self, connection):
        self.connection = connection
        multiprocessing.Process.__init__(self)
    
    def run(self):
        logging.info('Publisher process')
        for _ in range(20):
            self.connection.send(f'Hi from publisher process. { random.randint(1,100)} was sent')
            time.sleep(0.5)
        self.connection.send(None)
        self.connection.close()


class Subscriber(multiprocessing.Process):
    def __init__(self, connection):
        self.is_alive = True
        self.connection = connection
        multiprocessing.Process.__init__(self)
    
    def run(self):
        logging.info('Subscriber process')
        while self.is_alive:
            result = self.connection.recv()
            self.is_alive = result is not None
            logging.info(result)
        else:
            self.connection.close()



if __name__ == '__main__':
    conn1, conn2 = multiprocessing.Pipe()
    publisher = Publisher(conn1)
    subscriber = Subscriber(conn2)
    publisher.start()
    subscriber.start()


