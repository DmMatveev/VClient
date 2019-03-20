import commands
import pywinauto
from commands import utils
from common.common import CommandStatus
from common.proxy import ProxyAddParameters


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
        commands.application.Switch.switch_to_proxy()
        self.parameters = parameters
        super().__init__()

    @utils.wait_after(1)
    def execute(self):
        try:
            self.open_window()

            self.pane[self.BUTTON_EXPAND_PROXY_INPUT].click()

            self.write_data()

            self.pane[self.BUTTON_PROXY_ADD].click()
        except pywinauto.findwindows.ElementNotFoundError:
            return CommandStatus.ERROR

        except pywinauto.findwindows.ElementAmbiguousError:
            return CommandStatus.ERROR

        except RuntimeError:
            self.pane.child_window(control_type='Button', ctrl_index=-1).click()
            return CommandStatus.ERROR

        return CommandStatus.SUCCESS

    @commands.wait_before(1)
    def write_data(self):
        self.pane[self.INPUT_PROXY_IP].set_text(self.parameters.ip)
        self.pane[self.INPUT_PROXY_PORT].set_text(self.parameters.port)
        self.pane[self.INPUT_PROXY_LOGIN].set_text(self.parameters.login)
        self.pane[self.INPUT_PROXY_PASSWORD].set_text(self.parameters.password)

    @commands.wait_after(1)
    def open_window(self):
        self.pane[self.BUTTON_OPEN_WINDOW_PROXY].click()
