import pywinauto
from pywinauto import WindowSpecification

import commands


class Command:
    RPC = True

    app = pywinauto.Application(backend='uia')
    pane: WindowSpecification = None

    APP_DIR = 'C:\\Users\\Dmitry\\AppData\\Local\\VtopeBot'

    def __init__(self, *args):
        self._check_parameters(*args)

        self._data = self.execute()

    def _check_parameters(self, *parameters):
        parameters = list(parameters)
        for parameter in parameters:
            if not isinstance(parameter, str) or parameter == '':
                raise commands.InvalidParameters

    def execute(self):
        raise NotImplementedError

    def __getstate__(self):
        return self._data

    @property
    def result(self):
        return self._data
