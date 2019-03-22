import logging.config

import settings
from application import Application

log = logging.getLogger(__name__)

logging.config.dictConfig(settings.log_config)


def init():
    application = Application()
    application.connect()


if __name__ == '__main__':
    init()
