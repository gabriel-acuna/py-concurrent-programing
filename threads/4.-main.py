import logging



logging.basicConfig(
    level=logging.DEBUG,
    format=' Thread: %(thread)s - %(threadName)s -- %(message)s',
    )

if __name__ == '__main__':
    logging.debug('Hallo, ich bin im Hauptthread')