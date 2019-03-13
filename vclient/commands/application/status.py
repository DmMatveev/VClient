from enum import Enum, auto

import pywinauto

import commands
from status import WorkerStatus


class Status(commands.Command):
    def execute(self):
        if self.app.is_process_running():
            if self.is_ready():
                return WorkerStatus.READY

            if self.is_work():
                return WorkerStatus.WORK

            if self.is_not_auth():
                return WorkerStatus.NOT_AUTH

            return WorkerStatus.ERROR
        else:
            return WorkerStatus.STOP

    @commands.utils.wait_before(1)
    def is_ready(self):
        try:
            self.pane.child_window(title="Заработок не идет", control_type="Text").wrapper_object()
        except pywinauto.findwindows.ElementNotFoundError:
            return False
        except pywinauto.findwindows.ElementAmbiguousError:
            return False

        return True

    @commands.utils.wait_before(1)
    def is_work(self):
        return False
        try:
            self.pane.child_window(title="Регистрация", control_type="Button").wrapper_object()
        except pywinauto.findwindows.ElementNotFoundError:
            return False
        except pywinauto.findwindows.ElementAmbiguousError:
            return False

        return True

    @commands.utils.wait_before(1)
    def is_not_auth(self):
        try:
            self.pane.child_window(title="Регистрация", control_type="Button").wrapper_object()
        except pywinauto.findwindows.ElementNotFoundError:
            return False
        except pywinauto.findwindows.ElementAmbiguousError:
            return False

        return True
