import os
from typing import NamedTuple

import pywinauto
from common.common import ResultMessage, CommandStatus
from pywinauto import WindowSpecification


class Command:
    RPC = True

    app = pywinauto.Application(backend='uia')
    pane: WindowSpecification = None

    APP_DIR = f'{os.path.split(os.getenv("APPDATA"))[0]}\\Local\\VtopeBot'

    def __init__(self):
        try:
            result = self.execute()

        except pywinauto.findwindows.ElementNotFoundError:
            result = self.error_handler()

        except pywinauto.findwindows.ElementAmbiguousError:
            result = self.error_handler()

        except pywinauto.findbestmatch.MatchError:
            result = self.error_handler()

        except RuntimeError:
            result = self.error_handler()

        else:
            if self.is_error():
                result = CommandStatus.ERROR
                self.error_handler()

        try:
            self._status, self._data = result
        except TypeError:
            self._status = result
            self._data = None

    def execute(self):  # написать вовзврат двух аргументов
        raise NotImplementedError

    def error_handler(self):
        pass

    def is_error(self):
        return False

    @property
    def status(self) -> CommandStatus:
        return self._status

    @property
    def data(self) -> NamedTuple:
        return self._data

    @property
    def message(self):
        return ResultMessage(self._status, self._data)
