import pywinauto

import commands
from commands.account.get import AccountGetStatus
from common.account import AccountAddParameters, AccountAddStatus


class Add(commands.Command):
    BUTTON_OPEN_WINDOW_ACCOUNT = 'Button5'
    BUTTON_CLOSE_WINDOW_ACCOUNT = 'Button23'

    INPUT_ACCOUNT_LOGIN = 'Edit2'
    INPUT_ACCOUNT_PASSWORD = 'Edit1'

    BUTTON_ACCOUNT_ADD = 'Добавить аккаунт2'

    def __init__(self, parameters: AccountAddParameters):
        self.parameters = parameters
        super().__init__()

    def write_data(self):
        self.pane[self.INPUT_ACCOUNT_LOGIN].set_text(self.parameters.login)
        self.pane[self.INPUT_ACCOUNT_PASSWORD].set_text(self.parameters.password)

    @commands.wait_before(1)
    def is_account_add(self):
        if commands.account.Get(self.parameters.login).status == AccountGetStatus.FOUND:
            return True

        return False

    def choose_proxy(self):
        pass

    @commands.wait_after(1)
    def open_window(self):
        self.pane[self.BUTTON_OPEN_WINDOW_ACCOUNT].click()

    def execute(self):
        for _ in range(3):
            try:
                self.open_window()

                self.pane['Добавление аккаунтаCustom'].children()[0].click() # выбор типа аккаунта

                self.write_data()

                if self.parameters.proxy != '':
                    self.pane.child_window(title="Запускать только через прокси", control_type="CheckBox").click()
                    self.pane.child_window(title="Вручную", control_type="Button")

                self.pane[self.BUTTON_ACCOUNT_ADD].click()

                if self.is_account_add():
                    return AccountAddStatus.ADD

            except pywinauto.findwindows.ElementNotFoundError:
                return AccountAddStatus.ERROR

        return AccountAddStatus.ERROR_NOT_ADD
