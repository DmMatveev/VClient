import pywinauto

import commands


#TODO Бывает что не добавляется скоре всего из-за их сервера


class Add(commands.Command):
    BUTTON_OPEN_WINDOW_ACCOUNT = 'Button5'
    BUTTON_CLOSE_WINDOW_ACCOUNT = 'Button23'

    WINDOW_ACCOUNT = 'Custom27'
    INPUT_ACCOUNT_LOGIN = 'Edit2'
    INPUT_ACCOUNT_PASSWORD = 'Edit1'
    BUTTON_ACCOUNT_ADD = 'Добавить аккаунт2'

    def __init__(self, account_type, account_login, account_password, account_proxy_ip=None):
        super().__init__(account_type, account_login, account_password)

        self._account_type = account_type
        self._account_login = account_login
        self._account_password = account_password
        self._account_proxy_ip = account_proxy_ip

    def _write_data(self):
        self.pane[self.INPUT_ACCOUNT_LOGIN].set_text(self._account_login)
        self.pane[self.INPUT_ACCOUNT_PASSWORD].set_text(self._account_password)

    def execute(self):
        self.pane[self.BUTTON_OPEN_WINDOW_ACCOUNT].click()
        window = self.pane[self.WINDOW_ACCOUNT]

        try:
            window.wait('exists', timeout=5)
        except pywinauto.timings.TimeoutError:
            return -1#TODO сделать raise

        self._write_data()

        self.pane[self.BUTTON_ACCOUNT_ADD].click()
