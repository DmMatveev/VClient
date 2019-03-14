import commands
import pywinauto
from common import AuthStatus


class Auth(commands.Command):
    INPUT_LOGIN = 'Edit1'
    INPUT_PASSWORD = 'Edit2'

    TEXT_ERROR_NO_INTERNET = 'Отсутствует подключение к интернету'
    TEXT_ERROR_AUTH = 'Неверный логин или пароль'

    BUTTON_AUTH = 'Button3'

    def __init__(self, login, password):
        self._app_login = login
        self._app_password = password

        super().__init__(login, password)

    def _write_data(self):
        self.pane[self.INPUT_LOGIN].set_text(self._app_login)
        self.pane[self.INPUT_PASSWORD].set_text(self._app_password)

    @classmethod
    def is_auth(cls):
        try:
            cls.pane.child_window(title="Добавить аккаунт", control_type="Button").wrapper_object()
        except pywinauto.findwindows.ElementNotFoundError:
            return False

        return True

    def execute(self):
        if self.is_auth():
            return AuthStatus.ERROR_ALREADY_AUTH, None

        self._write_data()

        self.pane[self.BUTTON_AUTH].click()

        for _ in range(6):
            if self.is_auth():
                return AuthStatus.AUTH, None

        try:
            self.pane[self.TEXT_ERROR_AUTH].wait('exists', timeout=5)
        except pywinauto.application.TimeoutError:
            pass
        else:
            return AuthStatus.ERROR_LOGIN_OR_PASSWORD_INCORRECT, None

        try:
            self.pane[self.TEXT_ERROR_NO_INTERNET].wait('exists', timeout=5)
        except pywinauto.application.TimeoutError:
            pass
        else:
            return AuthStatus.ERROR_SERVER_NOT_RESPONSE, None

        return AuthStatus.ERROR, None
