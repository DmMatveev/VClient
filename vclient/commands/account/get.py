from enum import Enum, auto

import commands


class AccountGetStatus(Enum):
    FOUND = auto()
    NOT_FOUND = auto()


class Get(commands.Command):
    RPC = False

    def __init__(self, login):
        self.login = login

        super().__init__()

    def execute(self):
        accounts_info = commands.account.List.get_all_accounts_info()
        for account_info in accounts_info:
            if self.login in account_info:
                return AccountGetStatus.FOUND

        return AccountGetStatus.NOT_FOUND
