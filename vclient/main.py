import logging.config
import time

from application import Application
from pika.exceptions import ConnectionClosed, IncompatibleProtocolError

logging.config.dictConfig({
    'version': 1,
    'disable_existing_loggers': False,

    'formatters': {
        'standard': {
            'format': '%(asctime)s [%(levelname)s] %(name)s: %(message)s'
        },
    },

    'handlers': {
        'default': {
            'level': 'DEBUG',
            'formatter': 'standard',
            'class': 'logging.StreamHandler',
        }
    },
    'loggers': {
        '': {
            'handlers': ['default'],
            'level': 'DEBUG',
        },

        'pika': {
            'level': 'ERROR',
        }
    }
})

log = logging.getLogger(__name__)


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
