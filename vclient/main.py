import time

from vclient.application import Application


def init():
    application = Application()

    while True:
        try:
            print('Try connect to server')
            application.connect()
        except Exception as e:
            print(e)
            print('Server not response. Pause 60 second')
            time.sleep(60)


if __name__ == '__main__':
    init()
