import pywinauto
from pywinauto import WindowSpecification

import commands
from common import ResultMessage

import os


class Command:
    RPC = True

    app = pywinauto.Application(backend='uia')
    pane: WindowSpecification = None

    APP_DIR = f'{os.path.split(os.getenv("APPDATA"))[0]}\\Local\\VtopeBot'

    def __init__(self):
        self._status, self._data = self.execute()

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
