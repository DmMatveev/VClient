import os

import pywinauto

from src import commands

from .exceptions import *


class Stop(commands.Command):
    PROCESS = ['vtopementor.exe', 'vtopebot.exe', 'vtopeworker.exe', 'vtopeupdater.exe']

    def execute(self):
        path = os.path.join(commands.APPLICATION_DIRECTORY, self.APPLICATION)

        #TODO вручную закрыть и проверить все процесс

        commands.Command.pane = None