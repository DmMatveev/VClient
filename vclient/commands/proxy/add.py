import commands
import pywinauto
from commands.proxy.get import ProxyGetStatus
from common.proxy import ProxyAddParameters, ProxyAddStatus


class Add(commands.Command):
    BUTTON_OPEN_WINDOW_PROXY = 'Button9'
    BUTTON_CLOSE_WINDOW_PROXY = ''

    BUTTON_SWITCH_TO_PROXY = 'Button11'
    BUTTON_SWITCH_TO_ACCOUNT = 'Button8'

    BUTTON_EXPAND_PROXY_INPUT = 'Button17'

    INPUT_PROXY_IP = 'IP проксиEdit2'
    INPUT_PROXY_PORT = 'IP проксиEdit'
    INPUT_PROXY_LOGIN = 'Порт проксиEdit'
    INPUT_PROXY_PASSWORD = 'Логин (необязательно)Edit'

    BUTTON_PROXY_ADD = 'Подключить прокcи'

    def __init__(self, parameters: ProxyAddParameters):
        self.parameters = parameters

        self.switch_to_proxy()
        super().__init__()
        self.switch_to_account()

    @commands.wait_after(1)
    def switch_to_proxy(self):
        self.pane[self.BUTTON_SWITCH_TO_PROXY].click()

    @commands.wait_after(1)
    def switch_to_account(self):
        self.pane[self.BUTTON_SWITCH_TO_ACCOUNT].click()

    @commands.wait_before(1)
    def write_data(self):
        self.pane[self.INPUT_PROXY_IP].set_text(self.parameters.ip)
        self.pane[self.INPUT_PROXY_PORT].set_text(self.parameters.port)
        self.pane[self.INPUT_PROXY_LOGIN].set_text(self.parameters.login)
        self.pane[self.INPUT_PROXY_PASSWORD].set_text(self.parameters.password)

    @commands.wait_before(1)
    def is_proxy_add(self):
        if commands.proxy.Get(self.parameters.ip).status == ProxyGetStatus.FOUND:
            return True

        return False

    @commands.wait_after(1)
    def open_window(self):
        self.pane[self.BUTTON_OPEN_WINDOW_PROXY].click()

    def execute(self):
        for _ in range(3):
            try:
                self.open_window()

                self.pane[self.BUTTON_EXPAND_PROXY_INPUT].click()

                self.write_data()

                self.pane[self.BUTTON_PROXY_ADD].click()

                if self.is_proxy_add():
                    return ProxyAddStatus.ADD

            except pywinauto.findwindows.ElementNotFoundError:
                return ProxyAddStatus.ERROR

        return ProxyAddStatus.ERROR_NOT_ADD
