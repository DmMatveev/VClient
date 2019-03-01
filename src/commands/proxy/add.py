import pywinauto

from src import commands


class Add(commands.Command):
    BUTTON_OPEN_WINDOW_PROXY = ''
    BUTTON_CLOSE_WINDOW_PROXY = ''

    BUTTON_OPEN_LIST = ''

    WINDOW_PROXY = ''
    INPUT_PROXY_IP = ''
    INPUT_PROXY_PORT = ''
    INPUT_PROXY_LOGIN = ''
    INPUT_PROXY_PASSWORD = ''

    BUTTON_PROXY_ADD = ''

    def __init__(self, proxy_ip, proxy_port, proxy_login, proxy_password):
        self._check_parameters(proxy_ip, proxy_port, proxy_login, proxy_password)

        super().__init__()

        self._proxy_ip = proxy_ip
        self._proxy_port = proxy_port
        self._proxy_login = proxy_login
        self._proxy_password = proxy_password

    @staticmethod
    def _check_parameters(*parameters):
        parameters = list(parameters)

        for parameter in parameters:
            if not isinstance(parameter, str) or parameter == '':
                raise commands.InvalidParameters

    def _write_data(self):
        self.pane[self.INPUT_PROXY_IP].set_text(self._proxy_ip)
        self.pane[self.INPUT_PROXY_PORT].set_text(self._proxy_port)
        self.pane[self.INPUT_PROXY_LOGIN].set_text(self._proxy_login)
        self.pane[self.INPUT_PROXY_PASSWORD].set_text(self._proxy_password)

    def execute(self):
        self.pane[self.BUTTON_OPEN_WINDOW_PROXY].click()
        window = self.pane[self.WINDOW_PROXY]

        try:
            window.wait('exists', timeout=5)
        except pywinauto.timings.TimeoutError:
            return -1#TODO сделать raise

        self.pane[self.BUTTON_OPEN_LIST].click()

        self._write_data()

        self.pane[self.BUTTON_PROXY_ADD].click()

