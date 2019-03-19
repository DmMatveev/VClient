import commands
import pywinauto
from commands import utils
from common.application import ApplicationAuthParameters
from common.common import CommandStatus


class Auth(commands.Command):
    INPUT_LOGIN = 'Edit1'
    INPUT_PASSWORD = 'Edit2'

    TEXT_ERROR_NO_INTERNET = 'Отсутствует подключение к интернету'
    TEXT_ERROR_AUTH = 'Неверный логин или пароль'

    BUTTON_AUTH = 'Button3'

    def __init__(self, parameters: ApplicationAuthParameters):
        self.parameters = parameters
        super().__init__()

    def write_data(self):
        self.pane[self.INPUT_LOGIN].set_text(self.parameters.login)
        self.pane[self.INPUT_PASSWORD].set_text(self.parameters.password)

    @utils.wait_after(5)
    def confirm(self):
        self.pane[self.BUTTON_AUTH].click()

    def execute(self):
        try:
            self.write_data()
            self.confirm()

        except pywinauto.findwindows.ElementNotFoundError:
            return CommandStatus.ERROR

        except pywinauto.findwindows.ElementAmbiguousError:
            return CommandStatus.ERROR

        return CommandStatus.SUCCESS
