from enum import Enum

import commands
from commands import utils
from common.account import AccountInfo, AccountStatus, AccountType


class AccountTypeNumber(Enum):
    INSTAGRAM = 2
    VK = 1


class List(commands.Command):
    RPC = False

    def execute(self):
        list_box = self.pane.child_window(control_type='List', ctrl_index=0)
        return None, list(map(self.get_account_info, utils.get_all_items_info_string(list_box)))

    def get_account_info(self, account_info_string):
        account_info_string = utils.clean_info_string(account_info_string)

        status = self.get_account_status(account_info_string)
        account_info_string = self.clean_status(account_info_string, status)

        type_ = self.get_account_type(account_info_string)

        login = account_info_string[:-1]

        return AccountInfo(login, status, type_)

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
