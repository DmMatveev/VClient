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

    def __init__(self, *args):
        self._check_parameters(*args)

        self._status, self._data = self.execute()

    def _check_parameters(self, *parameters):
        parameters = list(parameters)
        for parameter in parameters:
            if not isinstance(parameter, str) or parameter == '':
                raise commands.InvalidParameters

    def execute(self):#написать вовзврат двух аргументов
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
