from enum import Enum

import commands
import pywinauto
from commands import utils
from common.account import AccountInfo, AccountStatus, AccountType
from common.common import CommandStatus


class AccountTypeNumber(Enum):  # Соответсиве типа аккаунта к номеру в строке
    INSTAGRAM = 2
    VK = 1


class List(commands.Command):
    def __init__(self):
        commands.application.Switch.switch_to_account()

        super().__init__()

    def execute(self):
        try:
            list_box = self.pane.child_window(control_type='List', ctrl_index=0)
            all_items_info_string = utils.get_all_items_info_string(list_box)

            if len(all_items_info_string) == 0:
                return CommandStatus.SUCCESS, []

            return CommandStatus.SUCCESS, list(map(self.get_account_info, all_items_info_string))

        except pywinauto.findwindows.ElementNotFoundError:
            return CommandStatus.ERROR

        except pywinauto.findwindows.ElementAmbiguousError:
            return CommandStatus.ERROR

    @classmethod
    def get_account_info(cls, account_info_string):
        account_info_string = utils.clean_info_string(account_info_string)

        status = cls.get_account_status(account_info_string)
        account_info_string = cls.clean_status(account_info_string, status)

        type_ = cls.get_account_type(account_info_string)

        login = account_info_string[:-1]

        return AccountInfo(login, status, type_)

    @staticmethod
    def get_account_status(account_info_string: str) -> AccountStatus:
        for status in AccountStatus:
            if status.name in account_info_string:
                return status

        raise AttributeError('Статус аккаунта не найден')

    @staticmethod
    def clean_status(account_info_string: str, status: AccountStatus):
        parts = account_info_string.split(status.name)
        if len(parts) == 2:
            return parts[1]

        return parts

    @staticmethod
    def get_account_type(account_info_string: str) -> AccountType:
        account_type_number = int(account_info_string[-1])
        for type_ in AccountTypeNumber:
            if type_.value == account_type_number:
                return AccountType[type_.name]
