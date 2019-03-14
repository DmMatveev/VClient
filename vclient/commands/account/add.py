import pywinauto

import commands
from common import AccountAddParameters


class Add(commands.Command):
    BUTTON_OPEN_WINDOW_ACCOUNT = 'Button5'
    BUTTON_CLOSE_WINDOW_ACCOUNT = 'Button23'

    INPUT_ACCOUNT_LOGIN = 'Edit2'
    INPUT_ACCOUNT_PASSWORD = 'Edit1'

    BUTTON_ACCOUNT_ADD = 'Добавить аккаунт2'

    def __init__(self, parameters: AccountAddParameters):
        self.parameters = parameters
        super().__init__()

    def _write_data(self):
        self.pane[self.INPUT_ACCOUNT_LOGIN].set_text(self.parameters.login)
        self.pane[self.INPUT_ACCOUNT_PASSWORD].set_text(self.parameters.password)

    #TODO так же сделать обнуление через клик по Item
    def execute(self):
        for _ in range(6):
            self.pane[self.BUTTON_OPEN_WINDOW_ACCOUNT].click()

            try:
                self._write_data()
            except pywinauto.findwindows.ElementNotFoundError:
                continue

        for _ in range(6):
            self.pane[self.BUTTON_ACCOUNT_ADD].click()

            try:
                self.pane[self.INPUT_ACCOUNT_LOGIN].wrapper_object()
                self.pane[self.INPUT_ACCOUNT_PASSWORD].wrapper_object()
            except pywinauto.findwindows.ElementNotFoundError:
                return



