import pywinauto
from vclient import commands


class AppAlreadyAuth(Exception):
    pass


class LoginOrPasswordIncorrect(Exception):
    pass


class ServerNotResponse(Exception):
    pass


class AuthError(Exception):
    pass


class Auth(commands.Command):
    INPUT_LOGIN = 'Edit1'
    INPUT_PASSWORD = 'Edit2'

    TEXT_ERROR_NO_INTERNET = 'Отсутствует подключение к интернету'
    TEXT_ERROR_AUTH = 'Неверный логин или пароль'

    BUTTON_AUTH = 'Button3'

    def __init__(self, app_login, app_password):
        self._app_login = app_login
        self._app_password = app_password

        super().__init__(app_login, app_password)

    def _write_data(self):
        self.pane[self.INPUT_LOGIN].set_text(self._app_login)
        self.pane[self.INPUT_PASSWORD].set_text(self._app_password)

    @classmethod
    def is_auth(cls):
        try:
            #TODO взять данные из команды account.add
            cls.pane.child_window(title="Добавить аккаунт", control_type="Button").wait('exists', timeout=5)
        except pywinauto.application.TimeoutError:
            return False

        return True

    def execute(self):
        if self.is_auth():
            raise AppAlreadyAuth

        self._write_data()

        self.pane[self.BUTTON_AUTH].click()

        for _ in range(6):
            if self.is_auth():
                return

        try:
            self.pane[self.TEXT_ERROR_AUTH].wait('exists', timeout=5)
        except pywinauto.application.TimeoutError:
            pass
        else:
            raise LoginOrPasswordIncorrect

        try:
            self.pane[self.TEXT_ERROR_NO_INTERNET].wait('exists', timeout=5)
        except pywinauto.application.TimeoutError:
            pass
        else:
            raise ServerNotResponse

        raise AuthError
