import commands


class AccountNotFound(Exception):
    pass


class Get(commands.Command):
    RPC = False

    def __init__(self, login):
        self.login = login

        super().__init__()

    def execute(self):
        accounts = commands.account.List().get_accounts()
        for account in accounts:
            info = account.element_info.name
            if self.login in info:
                return account.element_info

        raise AccountNotFound
