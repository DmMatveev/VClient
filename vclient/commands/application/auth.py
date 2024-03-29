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

    def execute(self):
        self.write_data()

        self.confirm()

        return CommandStatus.SUCCESS

    def write_data(self):
        self.pane[self.INPUT_LOGIN].set_text(self.parameters.login)
        self.pane[self.INPUT_PASSWORD].set_text(self.parameters.password)

    @utils.wait_after(30)
    def confirm(self):
        self.pane[self.BUTTON_AUTH].click()
