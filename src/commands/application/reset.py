import os

from src import commands

from .exceptions import ApplicationStart


class Reset(commands.Command):
    DB_FILES_MASK = ['vdata', 'vproxy', 'accs.data']

    def execute(self):
        if self.app.is_process_running():
            raise ApplicationStart

        files = os.listdir(self.APPLICATION_DIRECTORY)

        #TODO проверить когда нету прав и не удаляется файл

        for file in files:
            if any(map(file.endswith, self.DB_FILES_MASK)):
                path = os.path.join(self.APPLICATION_DIRECTORY, file)
                os.remove(path)
