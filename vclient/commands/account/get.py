from enum import Enum, auto
from typing import List

import commands
from common.account import AccountType, AccountInfo


class AccountGetStatus(Enum):
    FOUND = auto()
    NOT_FOUND = auto()


class Get(commands.Command):
    RPC = False

    def __init__(self, login: str, type_: AccountType):
        self.login = login
        self.type_ = type_
        super().__init__()

    def execute(self):
        accounts_info: List[AccountInfo] = commands.account.List().data
        for account_info in accounts_info:
            if self.login == account_info.login and self.type_ == account_info.type:
                return AccountGetStatus.FOUND

        return AccountGetStatus.NOT_FOUND
