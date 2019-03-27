import os

import commands
import pywinauto
from commands import utils
from common.common import CommandStatus


class Start(commands.Command):
    APP = 'vtopebot.exe'

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

            self.close_modal_window()

            return CommandStatus.SUCCESS

        try:
            app = self.app.start(path, work_dir=self.APP_DIR)
        except pywinauto.application.AppStartError:
            return CommandStatus.ERROR

        commands.Command.pane = app.Pane

        self.close_modal_window()

        return CommandStatus.SUCCESS

    @utils.wait_after(2)
    def close_modal_window(self):
        try:
            self.pane.child_window(title="backgroundModalWidget", control_type="Custom").wait('exists', timeout=30)
        except RuntimeError:
            return

        utils.wait(3)
        self.pane.child_window(control_type='Button', ctrl_index=-1).click()
