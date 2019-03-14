import os

import commands
import pywinauto
from common import StartStatus


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
            return StartStatus.ERROR_ALREADY_START, None

        try:
            app = self.app.start(path, work_dir=self.APP_DIR)
        except pywinauto.application.AppStartError:
            return StartStatus.START_ERROR, None

        commands.Command.pane = app.Pane

        return StartStatus.START, None
