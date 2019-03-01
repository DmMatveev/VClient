import os
import subprocess

import commands
import pywinauto

from .exceptions import *


class Start(commands.Command):
    APPLICATION = 'vtopebot.exe'

    def execute(self):
        path = os.path.join(self.APPLICATION_DIRECTORY, self.APPLICATION)

        if self.app.is_process_running():
            raise ApplicationAlreadyStart

        try:
            pane = self.app.start(path=path, work_dir=self.APPLICATION_DIRECTORY)
        except pywinauto.application.AppStartError:
            raise ApplicationStartError

        commands.Command.pane = pane
