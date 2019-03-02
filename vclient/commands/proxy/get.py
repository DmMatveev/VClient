from vclient import commands


class Get(commands.Command):
    def __init__(self, account_login):
        self._check_parameters(account_login)

        super().__init__()
        self._account_login = account_login

    @staticmethod
    def _check_parameters(*parameters):
        for parameter in parameters:
            if not isinstance(parameter, str) and parameter == '':
                raise commands.InvalidParameters

    def execute(self):
        accounts = src.commands.account.List().get_accounts()
        for account in accounts:
            info = account.element_info.name
            if self._account_login in info and info.endswith('widget'):
                return account.element_info

        raise commands.AccountNotFound
