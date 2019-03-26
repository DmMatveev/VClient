import logging.config
import logging

import settings
from application import Application

logging.config.dictConfig(settings.log_config)

log = logging.getLogger(__name__)


def init():
    application = Application()
    application.start()


if __name__ == '__main__':
    init()
