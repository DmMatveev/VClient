import commands
import pyautogui
from commands import utils
from common.common import CommandStatus
from common.proxy import ProxyDeleteParameters


class Delete(commands.Command):
    OFFSET_FROM_BUTTON = 54

    def __init__(self, parameters: ProxyDeleteParameters):
        commands.application.Switch.switch_to_proxy()
        self.parameters = parameters
        super().__init__()

    def execute(self):
        list_box = self.pane.child_window(control_type='List', ctrl_index=1)

        left, top, right, bottom = utils.select_item_in_list_box(
            list_box,
            self.parameters.ip,
            commands.proxy.List.get_proxy_info,
            'ip')

        pyautogui.click(right - self.OFFSET_FROM_BUTTON, top + (bottom - top) / 2)

        try:
            self.pane.child_window(title="УДАЛИТЬ", control_type="Button").wait('exists', timeout=5)
            self.delete_item()
        except RuntimeError:
            return CommandStatus.ERROR

        x, y = utils.get_list_box_coordinate_center(list_box)

        pyautogui.click(x, y)
        for _ in range(10):
            pyautogui.click(x, y)
            pyautogui.scroll(300)

        return CommandStatus.SUCCESS

    def error_handler(self):
        x, y = utils.get_list_box_coordinate_center(self.pane.child_window(control_type='List', ctrl_index=1))
        pyautogui.click(x, y)
        for _ in range(10):
            pyautogui.click(x, y)
            pyautogui.scroll(300)

    def is_error(self):
        try:
            self.pane.child_window(title="ИЗМЕНИТЬ", control_type="Button").wait_not('exists', timeout=3)
        except RuntimeError:
            return True

        return False

    @utils.wait_after(2)
    def delete_item(self):
        self.pane.child_window(title="УДАЛИТЬ", control_type="Button").click()
