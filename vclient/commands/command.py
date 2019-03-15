import os

import pywinauto
from common.common import ResultMessage
from pywinauto import WindowSpecification


class Command:
    RPC = True

    app = pywinauto.Application(backend='uia')
    pane: WindowSpecification = None

    APP_DIR = f'{os.path.split(os.getenv("APPDATA"))[0]}\\Local\\VtopeBot'

    def __init__(self):
        result = [self.execute()]
        if len(result) == 2:
            self._status, self._data = result
        else:
            self._status = result
            self._data = None

    def execute(self):  # написать вовзврат двух аргументов
        raise NotImplementedError

    @property
    def status(self):
        return self._status

    @property
    def data(self):
        return self._data

    @property
    def message(self):
        return ResultMessage(self._status, self._data)
