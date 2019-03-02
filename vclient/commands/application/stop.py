import psutil
from vclient import commands


class Stop(commands.Command):
    PROCESSES = ['vtopementor.exe', 'vtopebot.exe', 'vtopeworker.exe', 'vtopeupdater.exe']

    def _get_processes(self):
        processes = [p for p in psutil.process_iter() if p.name() in self.PROCESSES]
        return processes

    def execute(self):
        for p in self._get_processes():
            parent = psutil.Process(p.pid)
            parent.kill()

        commands.Command.pane = None
