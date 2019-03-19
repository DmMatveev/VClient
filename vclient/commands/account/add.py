from enum import Enum

import commands
import pyautogui
import pywinauto
from commands.utils import get_items_info, get_list_box_coordinate_center
from common.account import AccountAddParameters, AccountAddStatus
# Соответсвие номера кнопки в типом аккаунта
from common.common import CommandStatus


class AccountTypeNumber(Enum):
    INSTAGRAM = 0
    VK = 1


class Add(commands.Command):
    INPUT_ACCOUNT_LOGIN = 'Edit2'
    INPUT_ACCOUNT_PASSWORD = 'Edit1'

    BUTTON_ACCOUNT_ADD = 'Добавить аккаунт2'

    def __init__(self, parameters: AccountAddParameters):
        commands.application.Switch.switch_to_account()

        self.parameters = parameters
        super().__init__()

    def execute(self):
        try:
            self.open_window()

            self.choose_type_account()

            self.write_data()

            if self.parameters.proxy != '':
                self.choose_proxy()

            self.pane[self.BUTTON_ACCOUNT_ADD].click()

        except pywinauto.findwindows.ElementNotFoundError:
            return AccountAddStatus.ERROR

        except pywinauto.findwindows.ElementAmbiguousError:
            return AccountAddStatus.ERROR

        return CommandStatus.SUCCESS

    def select_proxy(self, select_proxy_ip: str):
        def choose_proxy(left, top, right, bottom):
            pyautogui.click(left + 15, int(top + (bottom - top) / 2) - 5)

        list_box = self.pane['ПарольListBox']

        found_item = None

        items = get_items_info(list_box)

        first_item = items[0].name
        last_item = items[-1].name

        x, y = get_list_box_coordinate_center(list_box)
        while True:
            for item in items:
                if select_proxy_ip == commands.proxy.List.get_proxy_info(item.name).ip:
                    found_item = True

                    list_box_rectangle = list_box.rectangle()
                    list_box_top = list_box_rectangle.top
                    list_box_bottom = list_box_rectangle.bottom

                    found_item_rectangle = item.rectangle
                    found_item_top = found_item_rectangle.top
                    found_item_bottom = found_item_rectangle.bottom

                    if found_item_top < list_box_top:
                        pyautogui.click(x, y)
                        pyautogui.scroll(50)

                    elif found_item_bottom > list_box_bottom:
                        pyautogui.click(x, y)
                        pyautogui.scroll(-50)

                    else:
                        rectangle = item.rectangle
                        function_click(rectangle.left,
                                       rectangle.top,
                                       rectangle.right,
                                       rectangle.bottom)

                        return

                    items = get_items_info(list_box)
                    for item in items:
                        if find_item_name == commands.proxy.List.get_proxy_info(item.name).ip:
                            rectangle = item.rectangle
                            function_click(rectangle.left,
                                           rectangle.top,
                                           rectangle.right,
                                           rectangle.bottom)
                            return

            if found_item or items[-1] == last_item:
                break

            last_item = items[-1]

            pyautogui.click(x, y)
            pyautogui.scroll(-1000)
            pyautogui.move(0, 0)

            items = get_items_info(list_box)

    def choose_proxy(self):

        self.pane.child_window(title="Запускать только через прокси", control_type="CheckBox").click()

        self.pane.child_window(title="    Вручную", control_type="Button").click()

        self.select_proxy(select_proxy)

    def choose_type_account(self):
        window = self.pane.child_window(title="backgroundModalWidget", control_type="Custom")
        button_lists = window.parent().children()[1].children()[0].children()[0].children()

        button_lists[AccountTypeNumber[self.parameters.type.name].value].click()

    def write_data(self):
        self.pane[self.INPUT_ACCOUNT_LOGIN].set_text(self.parameters.login)
        self.pane[self.INPUT_ACCOUNT_PASSWORD].set_text(self.parameters.password)

    @commands.wait_after(1)
    def open_window(self):
        self.pane.child_window(title="Добавить аккаунт", control_type="Button").click()
