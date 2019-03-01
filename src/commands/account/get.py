import commands


class Get(commands.Command):
    def __init__(self, account_login):
        super().__init__(account_login)

        self._account_login = account_login

    def execute(self):
        accounts = commands.account.List().get_accounts()
        for account in accounts:
            info = account.element_info.name
            if self._account_login in info and info.endswith('widget'):
                return account.element_info

        raise commands.AccountNotFound
