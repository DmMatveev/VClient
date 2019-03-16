from enum import Enum

import commands
import pyautogui
from commands import utils
from common.account import AccountInfo, AccountStatus, AccountType


class AccountTypeNumber(Enum):
    INSTAGRAM = 2
    VK = 1

class List(commands.Command):
    RPC = False

    def get_list_box_children(self):
        return self.pane.child_window(control_type='List', ctrl_index=0).children()

    def get_list_box_coordinate_center(self):
        list_box = self.pane.child_window(control_type='List', ctrl_index=0)

        list_box_coordinate = list_box.rectangle()
        x = list_box_coordinate.left + (list_box_coordinate.right - list_box_coordinate.left) / 2
        y = list_box_coordinate.top + (list_box_coordinate.bottom - list_box_coordinate.top) / 2

        return x, y

    def get_accounts_info_string(self):
        def get_name_widget(widget):
            return widget.element_info.name

        elements = self.get_list_box_children()

        elements = [element.element_info.name for element in elements]

        accounts_name = [element for element in elements if element.endswith('widget')]

        return accounts_name

    @commands.utils.wait_before(1)
    def get_all_accounts_info_string(self):
        accounts_info = self.get_accounts_info_string()

        first_item = accounts_info[0]
        last_item = accounts_info[-1]

        accounts = set(accounts_info)

        x, y = self.get_list_box_coordinate_center()

        while True:
            pyautogui.click(x, y)
            pyautogui.scroll(-1000)
            accounts_info = self.get_accounts_info_string()
            accounts = accounts.union(accounts_info)

            if accounts_info[-1] == last_item:
                break

            last_item = accounts_info[-1]

        while True:
            pyautogui.click(x, y)
            pyautogui.scroll(1000)
            accounts_info = self.get_accounts_info_string()

            if accounts_info[0] == first_item:
                break

        return accounts

    def get_account_status(self, account_info: str) -> AccountStatus:
        for status in AccountStatus:
            if status.name in account_info:
                return status

        raise AttributeError('Статус аккаунта не найден')

    def clean_status(self, account_info: str, status: AccountStatus):
        return account_info.replace(status.name, '')[1:]

    def get_account_type(self, account_info: str) -> AccountType:
        account_type_number = int(account_info[-1])
        for type_ in AccountTypeNumber:
            if type_.value == account_type_number:
                return AccountType[type_.name]

    def get_account_info(self, account_info_string):
        account_info_string = account_info_string[:account_info_string.find('_____')]
        account_info_string = utils.clean_info_string(account_info_string)

        status = self.get_account_status(account_info_string)
        account_info_string = self.clean_status(account_info_string, status)

        type_ = self.get_account_type(account_info_string)

        login = account_info_string[:-1]

        return AccountInfo(login, status, type_)

    def execute(self):
        return None, list(map(self.get_account_info, self.get_all_accounts_info_string()))
