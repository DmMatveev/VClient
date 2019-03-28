import locale
import logging
import logging.config

import settings
from application import Application

logging.config.dictConfig(settings.log_config)

log = logging.getLogger(__name__)


def getpreferredencoding(do_setlocale=True):
    return "utf-8"


locale.getpreferredencoding = getpreferredencoding


def init():
    application = Application()
    application.start()


if __name__ == '__main__':
    init()
