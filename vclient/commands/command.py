import pywinauto

import vclient.commands as commands


class Command:
    app = pywinauto.Application(backend='uia')
    pane = None

    APP_DIR = 'C:\\Users\\Dmitry\\AppData\\Local\\VtopeBot'

    def __init__(self, *args):
        self._check_parameters(*args)

        self.data = None

        self.execute()

    def _check_parameters(self, *parameters):
        parameters = list(parameters)
        for parameter in parameters:
            if not isinstance(parameter, str) or parameter == '':
                raise commands.InvalidParameters

    def execute(self):
        raise NotImplementedError

    @property
    def result(self):
        return self.data
