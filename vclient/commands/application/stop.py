import logging

import commands
import psutil
from common.common import CommandStatus

log = logging.getLogger(__name__)


class Stop(commands.Command):
    PROCESSES = ['vtopementor.exe', 'vtopebot.exe', 'vtopeworker.exe', 'vtopeupdater.exe']

    def get_processes(self):
        processes = [p for p in psutil.process_iter() if p.name() in self.PROCESSES]
        return processes

    def execute(self):
        for p in self.get_processes():
            parent = psutil.Process(p.pid)
            parent.kill()

        commands.Command.pane = None

        return CommandStatus.SUCCESS
