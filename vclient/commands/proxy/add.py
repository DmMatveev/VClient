import commands
import pywinauto
from commands import utils
from common.common import CommandStatus
from common.proxy import ProxyAddParameters


class Add(commands.Command):
    BUTTON_EXPAND_PROXY_INPUT = 'Button17'

    INPUT_PROXY_IP = 'IP проксиEdit2'
    INPUT_PROXY_PORT = 'IP проксиEdit'
    INPUT_PROXY_LOGIN = 'Порт проксиEdit'
    INPUT_PROXY_PASSWORD = 'Логин (необязательно)Edit'

    def __init__(self, parameters: ProxyAddParameters):
        commands.application.Switch.switch_to_proxy()
        self.parameters = parameters
        super().__init__()

    def execute(self):
        self.open_window()

        self.expand_additional_field()

        self.write_data()

        self.save()

        return CommandStatus.SUCCESS

    def is_error(self):
        try:
            self.pane.child_window(title="backgroundModalWidget", control_type="Custom").wait_not('exists', timeout=3)
        except RuntimeError:
            return True

        return False

    @utils.wait_after(1)
    def error_handler(self):
        self.pane.child_window(control_type='Button', ctrl_index=-1).click()

    @utils.wait_after(1)
    def open_window(self):
        self.pane.child_window(title="Добавить прокси", control_type="Button").click()

    @utils.wait_after(0.5)
    def expand_additional_field(self):
        self.pane.child_window(title="ввести логин и пароль", control_type="Button").click()

    def write_data(self):
        self.pane[self.INPUT_PROXY_IP].set_text(self.parameters.ip)
        self.pane[self.INPUT_PROXY_PORT].set_text(self.parameters.port)
        self.pane[self.INPUT_PROXY_LOGIN].set_text(self.parameters.login)
        self.pane[self.INPUT_PROXY_PASSWORD].set_text(self.parameters.password)

    @utils.wait_after(1.5)
    def save(self):
        self.pane.child_window(title="Подключить прокcи", control_type="Button").click()
