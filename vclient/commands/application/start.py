import os
from enum import Enum, auto

import pywinauto

import commands


class Status(Enum):
    ALREADY_START = auto()
    START_ERROR = auto()
    START_SUCCESS = auto()


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
            return Status.ALREADY_START

        try:
            app = self.app.start(path, work_dir=self.APP_DIR)
        except pywinauto.application.AppStartError:
            return Status.START_ERROR.name

        commands.Command.pane = app.Pane

        return Status.START_SUCCESS.name
