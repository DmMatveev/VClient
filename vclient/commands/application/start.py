import os

import commands
import pywinauto
from common.common import CommandStatus


class Start(commands.Command):
    APP = 'vtopebot.exe'

    @commands.utils.wait_after(15)
    def execute(self):
        path = os.path.join(self.APP_DIR, self.APP)

        if self.app.is_process_running():
            return CommandStatus.ERROR

        try:
            app = self.app.connect(path=path)
        except pywinauto.application.ProcessNotFoundError:
            pass
        else:
            commands.Command.pane = app.Pane
            return CommandStatus.SUCCESS

        try:
            app = self.app.start(path, work_dir=self.APP_DIR)
        except pywinauto.application.AppStartError:
            return CommandStatus.ERROR

        commands.Command.pane = app.Pane

        return CommandStatus.SUCCESS

