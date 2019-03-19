import commands
import pywinauto
from common.application import ApplicationStatus
from common.common import CommandStatus


class Status(commands.Command):
    TEXT_ERROR_NO_INTERNET = ''

    TEXT_ERROR_AUTH = 'Неверный логин или пароль'

    def execute(self):
        if self.app.is_process_running():
            if self.is_ready():
                return CommandStatus.SUCCESS, ApplicationStatus.READY

            if self.is_work():
                return CommandStatus.SUCCESS, ApplicationStatus.READY

            if self.is_not_auth():
                try:
                    self.pane.child_window(title="Неверный логин или пароль", control_type="Text").wrapper_object()
                except pywinauto.findwindows.ElementNotFoundError:
                    pass
                except pywinauto.findwindows.ElementAmbiguousError:
                    pass
                else:
                    return CommandStatus.SUCCESS, ApplicationStatus.AUTH_LOGIN_OR_PASSWORD_INCORRECT

                try:
                    self.pane.child_window(title="Отсутствует подключение к интернету",
                                           control_type="Text").wrapper_object()
                except pywinauto.findwindows.ElementNotFoundError:
                    pass
                except pywinauto.findwindows.ElementAmbiguousError:
                    pass
                else:
                    return CommandStatus.SUCCESS, ApplicationStatus.SERVER_NOT_RESPONSE

                return CommandStatus.ERROR

            return CommandStatus.ERROR

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
    def is_not_auth(self):
        try:
            self.pane.child_window(title="Регистрация", control_type="Button").wrapper_object()
        except pywinauto.findwindows.ElementNotFoundError:
            return False
        except pywinauto.findwindows.ElementAmbiguousError:
            return False

        return True

    @commands.utils.wait_before(1)
    def is_work(self):
        return True
