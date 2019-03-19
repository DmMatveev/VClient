import logging.config
import time

import settings
from application import Application
from pika.exceptions import ConnectionClosed, IncompatibleProtocolError

log = logging.getLogger(__name__)

logging.config.dictConfig(settings.log_config)


def init():
    application = Application()
    while True:
        try:
            application.connect()
        except ConnectionClosed:
            log.debug('RabbitMq connection broken')
            time.sleep(5)

        except IncompatibleProtocolError:
            log.debug('RabbitMq connection broken')
            time.sleep(5)

        except Exception as e:
            log.exception('')


if __name__ == '__main__':
    init()
