import os

import commands

from common import ResetStatus


class Reset(commands.Command):
    FILES = ['vdata', 'vproxy', 'accs.data']

    def execute(self):
        if self.app.is_process_running():
            return ResetStatus.ERROR_APP_START, None

        try:
            files = os.listdir(self.APP_DIR)

            for file in files:
                if any(map(file.endswith, self.FILES)):
                    path = os.path.join(self.APP_DIR, file)
                    os.remove(path)
        except Exception:
            return ResetStatus.ERROR, None

        return ResetStatus.RESET, None
