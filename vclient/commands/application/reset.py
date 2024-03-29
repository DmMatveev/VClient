import os

import commands
from common.common import CommandStatus


class Reset(commands.Command):
    FILES = ['vdata', 'vproxy', 'accs.data']

    def execute(self):
        if self.app.is_process_running():
            return CommandStatus.ERROR

        try:
            files = os.listdir(self.APP_DIR)

            for file in files:
                if any(map(file.endswith, self.FILES)):
                    path = os.path.join(self.APP_DIR, file)
                    os.remove(path)
        except Exception:
            return CommandStatus.ERROR

        return CommandStatus.SUCCESS
