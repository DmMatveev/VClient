import pywinauto

import commands
from common import AccountAddParameters, AccountAddStatus


class Add(commands.Command):
    BUTTON_OPEN_WINDOW_ACCOUNT = 'Button5'
    BUTTON_CLOSE_WINDOW_ACCOUNT = 'Button23'

    INPUT_ACCOUNT_LOGIN = 'Edit2'
    INPUT_ACCOUNT_PASSWORD = 'Edit1'

    BUTTON_ACCOUNT_ADD = 'Добавить аккаунт2'

    def __init__(self, parameters: AccountAddParameters):
        self.parameters = parameters
        super().__init__()

    @commands.wait_before(3)
    def is_account_add(self):
        try:
            commands.account.Get(self.parameters.login)
        except commands.account.AccountNotFound:
            return False

        return True

    def write_data(self):
        self.pane[self.INPUT_ACCOUNT_LOGIN].set_text(self.parameters.login)
        self.pane[self.INPUT_ACCOUNT_PASSWORD].set_text(self.parameters.password)

    def execute(self):
        self.pane[self.BUTTON_OPEN_WINDOW_ACCOUNT].click()

        try:
            self.write_data()
        except pywinauto.findwindows.ElementNotFoundError:
            return AccountAddStatus.ERROR, None

        self.pane[self.BUTTON_ACCOUNT_ADD].click()

        if self.is_account_add():
            return AccountAddStatus.ADD, None

        return AccountAddStatus.ERROR, None
