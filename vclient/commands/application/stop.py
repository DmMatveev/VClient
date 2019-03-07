import psutil
from vclient import commands

from vclient.status import StopStatus


class Stop(commands.Command):
    PROCESSES = ['vtopementor.exe', 'vtopebot.exe', 'vtopeworker.exe', 'vtopeupdater.exe']

    def _get_processes(self):
        processes = [p for p in psutil.process_iter() if p.name() in self.PROCESSES]
        return processes

    def execute(self):
        try:
            for p in self._get_processes():
                parent = psutil.Process(p.pid)
                parent.kill()

            commands.Command.pane = None
        except Exception:
            return StopStatus.ERROR

        return StopStatus.STOP
