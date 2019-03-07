import pywinauto

from vclient import commands


class AccountNotAdd(Exception):
    pass


class Add(commands.Command):
    BUTTON_OPEN_WINDOW_ACCOUNT = 'Button5'
    BUTTON_CLOSE_WINDOW_ACCOUNT = 'Button23'

    WINDOW_ACCOUNT = 'Custom27'
    INPUT_ACCOUNT_LOGIN = 'Edit2'
    INPUT_ACCOUNT_PASSWORD = 'Edit1'

    BUTTON_ACCOUNT_ADD = 'Добавить аккаунт2'

    def __init__(self, account_type, account_login, account_password, account_proxy_ip=None):
        self._account_type = account_type
        self._account_login = account_login
        self._account_password = account_password
        self._account_proxy_ip = account_proxy_ip

        super().__init__(account_type, account_login, account_password)

    def _write_data(self):
        self.pane[self.INPUT_ACCOUNT_LOGIN].set_text(self._account_login)
        self.pane[self.INPUT_ACCOUNT_PASSWORD].set_text(self._account_password)

    def _is_account_add(self):
        try:
            commands.account.Get(self._account_login)
        except commands.account.AccountNotFound:
            return False

        return True

    #TODO так же сделать обнуление через клик по Item
    def execute(self):
        for _ in range(6):
            self.pane[self.BUTTON_OPEN_WINDOW_ACCOUNT].click()
            window = self.pane[self.WINDOW_ACCOUNT]

            try:
                window.wait('exists', timeout=5)
            except pywinauto.application.TimeoutError:
                raise commands.WindowNotOpen

            self._write_data()

            self.pane[self.BUTTON_ACCOUNT_ADD].click()

            if self._is_account_add():
                return

        raise AccountNotAdd



