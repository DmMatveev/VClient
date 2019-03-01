import pywinauto

import commands


class Command:
    app = pywinauto.Application(backend='uia')
    pane = None

    def __init__(self, *args, **kwargs):
        if self.pane is None and not isinstance(self.pane, pywinauto.Application):
            raise Exception('Not set pane variable')

        self._check_parameters()

    def _check_parameters(self, *parameters):
        for parameter in parameters:
            if not isinstance(parameter, str) or parameter == '':
                raise commands.InvalidParameters

    @property
    def APPLICATION_DIRECTORY(self):
        return 'C:\\Users\\Dmitry\\AppData\\Local\\VtopeBot'

    def execute(self):
        raise NotImplementedError
