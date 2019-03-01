import pywinauto
from commands.application import ExceptionAuth, ExceptionInternet
from src import commands

import time


class Auth(commands.Command):
    INPUT_LOGIN = ''
    INPUT_PASSWORD = ''

    BUTTON_AUTH = ''

    def __init__(self, app_login, app_password):
        super().__init__(app_login, app_password)

        self._app_login = app_login
        self._app_password = app_password

    def _write_data(self):
        self.pane[self.INPUT_LOGIN].set_text(self._app_login)
        self.pane[self.INPUT_PASSWORD].set_text(self._app_password)

    def execute(self):
        self._write_data()

        self.pane[self.BUTTON_AUTH].click()



        # 5 * 6 = 30 секунд ожидание авторизации
        if any([self.is_auth()] * 6):
            return True

        try:
            self._app.Pane[self.TEXT_ERROR_AUTH].wait('exists', timeout=3)
        except pywinauto.timings.TimeoutError:
            pass
        else:
            raise ExceptionAuth('')

        try:
            self._app.Pane[self.TEXT_ERROR_NO_INTERNET].wait('exists', timeout=3)
        except pywinauto.timings.TimeoutError:
            pass
        else:
            raise ExceptionInternet

        return False


#class CheckAuth(commands.Command):
#    def execute(self):
#        auth_label = self.app.child_window(title="Логин втопе", control_type="Text")
#
#        #TODO либо то, либо другое, либо ожиданиео
#
#        try:
#            auth_label.wait('exists', timeout=5)
#        except pywinauto.timings.TimeoutError:
#            return True
#
#        try:
#            auth_label.wait('exists', timeout=5)
#        except pywinauto.timings.TimeoutError:
#            return True
#
#
#        return False
