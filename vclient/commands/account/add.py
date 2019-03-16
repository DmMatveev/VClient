from enum import Enum

import commands
import pywinauto
from commands.account.get import AccountGetStatus
from common.account import AccountAddParameters, AccountAddStatus
from pywinauto import WindowSpecification


class AccountTypeNumber(Enum):
    INSTAGRAM = 0
    VK = 1


class Add(commands.Command):
    INPUT_ACCOUNT_LOGIN = 'Edit2'
    INPUT_ACCOUNT_PASSWORD = 'Edit1'

    BUTTON_ACCOUNT_ADD = 'Добавить аккаунт2'

    def __init__(self, parameters: AccountAddParameters):
        self.parameters = parameters
        super().__init__()

    def execute(self):
        for _ in range(3):
            try:
                self.open_window()

                self.choose_type_account()

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

    @commands.wait_after(1)
    def open_window(self):
        self.pane.child_window(title="Добавить аккаунт", control_type="Button").click()

    def choose_type_account(self):
        window = self.pane.child_window(title="backgroundModalWidget", control_type="Custom")
        button_lists = window.parent().children()[1].children()[0].children()[0].children()

        button_lists[AccountTypeNumber[self.parameters.type.name].value].click()

    def write_data(self):
        self.pane[self.INPUT_ACCOUNT_LOGIN].set_text(self.parameters.login)
        self.pane[self.INPUT_ACCOUNT_PASSWORD].set_text(self.parameters.password)

    def choose_proxy(self):
        pass

    @commands.wait_before(1)
    def is_account_add(self):
        account_get_status = commands.account.Get(self.parameters.login, self.parameters.type).status

        if account_get_status == AccountGetStatus.FOUND:
            return True

        return False
