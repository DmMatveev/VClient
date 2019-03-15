import os

import commands
import pywinauto
from common.common import StartStatus


class Start(commands.Command):
    APP = 'vtopebot.exe'

    @commands.utils.wait_after(1)
    def execute(self):
        path = os.path.join(self.APP_DIR, self.APP)

        if self.app.is_process_running():
            return StartStatus.ERROR_ALREADY_START

        try:
            app = self.app.connect(path=path)
        except pywinauto.application.ProcessNotFoundError:
            pass
        else:
            commands.Command.pane = app.Pane
            return StartStatus.START

        try:
            app = self.app.start(path, work_dir=self.APP_DIR)
        except pywinauto.application.AppStartError:
            return StartStatus.START_ERROR

        commands.Command.pane = app.Pane
        return StartStatus.START
