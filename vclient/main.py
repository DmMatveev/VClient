import os
import sys
import time

from output import output

from vclient.application import Application


def init():
    application = Application()

    while True:
        try:
            output.flush('Connect')
            application.connect()
        except Exception as e:
            output.flush('Connect Failed. Pause 60 sec')
            time.sleep(60)


if __name__ == '__main__':
    init()
