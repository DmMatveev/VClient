import logging
import time

from application import Application
from pika.exceptions import ConnectionClosed, IncompatibleProtocolError

#logging.basicConfig(level=logging.DEBUG)


def init():
    print('Start')
    application = Application()
    while True:
        try:
            application.connect()
        except ConnectionClosed:
            print('Connect Failed')
            time.sleep(5)

        except IncompatibleProtocolError:
            print('Connect Failed')
            time.sleep(5)

        except Exception as e:
            print(e)


if __name__ == '__main__':
    init()
