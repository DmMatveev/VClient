import pywinauto

import commands

#TODO Бывает что не добавляется скоре всего из-за их сервера


class Add(commands.Command):
    BUTTON_OPEN_ACCOUNT = 'Button5'
    BUTTON_CLOSE_ACCOUNT = 'Button23'

    WINDOW_ACCOUNT = 'Custom27'
    INPUT_ACCOUNT_LOGIN = 'Edit2'
    INPUT_ACCOUNT_PASSWORD = 'Edit1'
    BUTTON_ACCOUNT_ADD = 'Добавить аккаунт2'

    def __init__(self, account_type, account_login, account_password, account_proxy_ip=None):
        self._check_parameters(account_type, account_login, account_password, account_proxy_ip)

        super().__init__()

        self._account_type = account_type
        self._account_login = account_login
        self._account_password = account_password
        self._account_proxy_ip = account_proxy_ip

    @staticmethod
    def _check_parameters(*parameters):
        parameters = list(parameters)
        account_proxy_ip = parameters.pop()

        for parameter in parameters:
            if not isinstance(parameter, str) or parameter == '':
                raise commands.InvalidParameters

    def _write_data(self):
        self.pane[self.INPUT_ACCOUNT_LOGIN].set_text(self._account_login)
        self.pane[self.INPUT_ACCOUNT_PASSWORD].set_text(self._account_password)

    def execute(self):
        self.pane[self.BUTTON_OPEN_ACCOUNT].click()
        widget = self.pane[self.WINDOW_ACCOUNT]

        try:
            widget.wait('exists', timeout=5)
        except pywinauto.timings.TimeoutError:
            return -1#TODO сделать raise

        self._write_data()

        self.pane[self.BUTTON_ACCOUNT_ADD].click()
