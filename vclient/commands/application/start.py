import os
import time

import pywinauto

import vclient.commands as commands


class ApplicationStartError(Exception):
    pass


class ApplicationAlreadyStart(Exception):
    pass


class ApplicationStart(Exception):
    pass


class Start(commands.Command):
    APP = 'vtopebot.exe'

    @commands.utils.wait_after(10)
    def execute(self):
        path = os.path.join(self.APP_DIR, self.APP)

        try:
            self.app.connect(path=path)
        except pywinauto.application.ProcessNotFoundError:
            pass
        else:
            raise ApplicationAlreadyStart

        try:
            app = self.app.start(path, work_dir=self.APP_DIR)
        except pywinauto.application.AppStartError:
            raise ApplicationStartError

        commands.Command.pane = app.Pane
