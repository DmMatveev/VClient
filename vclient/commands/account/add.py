from enum import Enum

import commands
import pyautogui
import pywinauto.timings
from commands import utils
from common.account import AccountAddParameters
from common.common import CommandStatus


# Соответсвие номера кнопки c типом аккаунта
class AccountTypeNumber(Enum):
    INSTAGRAM = 0
    VK = 1


class Add(commands.Command):
    INPUT_ACCOUNT_LOGIN = 'Edit2'
    INPUT_ACCOUNT_PASSWORD = 'Edit1'

    def __init__(self, parameters: AccountAddParameters):
        commands.application.Switch.switch_to_account()
        self.parameters = parameters
        super().__init__()

    def execute(self):
        self.open_window()

        self.choose_account_type()

        self.write_data()

        if self.parameters.proxy != '':
            self.choose_proxy()

        self.save()

        return CommandStatus.SUCCESS

    def is_error(self):
        try:
            self.pane.child_window(title="backgroundModalWidget", control_type="Custom").wait_not('exists', timeout=3)
        except RuntimeError:
            return True

        return False

    @utils.wait_after(1)
    def error_handler(self):
        self.pane.child_window(control_type='Button', ctrl_index=-1).click()

    @commands.wait_after(1)
    def open_window(self):
        self.pane.child_window(title="Добавить аккаунт", control_type="Button", ctrl_index=0).click()

    @commands.wait_after(0.5)
    def choose_account_type(self):
        window = self.pane.child_window(title="backgroundModalWidget", control_type="Custom")
        button_lists = window.parent().children()[1].children()[0].children()[0].children()

        button_lists[AccountTypeNumber[self.parameters.type.name].value].click()

    def write_data(self):
        self.pane[self.INPUT_ACCOUNT_LOGIN].set_text(self.parameters.login)
        self.pane[self.INPUT_ACCOUNT_PASSWORD].set_text(self.parameters.password)

    def choose_proxy(self):
        self.pane.child_window(title="Запускать только через прокси", control_type="CheckBox").click()

        self.choose_proxy_manual()

        self.select_proxy()

    def save(self):
        self.pane.child_window(title="Добавить аккаунт", control_type="Button", ctrl_index=1).click()

    @utils.wait_before(0.5)
    def choose_proxy_manual(self):
        self.pane.child_window(title="    Вручную", control_type="Button").click()

    @utils.wait_before(1)
    def select_proxy(self):
        left, top, _, bottom = utils.select_item_in_list_box(self.pane['ПарольListBox'],
                                                             self.parameters.proxy,
                                                             commands.proxy.List.get_proxy_info,
                                                             'ip')

        pyautogui.click(left + 15, int(top + (bottom - top) / 2) - 5)
