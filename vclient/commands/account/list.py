from enum import Enum
from typing import NamedTuple

import commands
import pyautogui


class AccountInfo(NamedTuple):
    login: str
    status: str
    type: str


class AccountStatus(Enum):
    badauth = 'Ошибка авторизации'


class List(commands.Command):
    STEP_SCROLL = 0

    ACCOUNT_STATUS = ['badauth', 'validating', 'manual']

    def _check_status(self, info):
        for status in self.ACCOUNT_STATUS:
            if status in info:
                return status

        raise Exception()

    @staticmethod
    def clean_login(login: str) -> str:
        """
        Хак, появляются рандомные числа в наименование
        Закономерность, что эти числа заканичвается одинаково и они одинакового размера
        """
        if '_' in login:
            number_size = login.rindex('_') - login.index('_') - 1
            login = login[number_size * 2 + 2:]

        return login

    @classmethod
    def get_list_box_children(cls):
        return cls.pane.child_window(control_type='List', ctrl_index=0).children()

    @classmethod
    def get_list_box_coordinate_center(cls):
        list_box = cls.pane.child_window(control_type='List', ctrl_index=0)

        list_box_coordinate = list_box.rectangle()
        x = list_box_coordinate.left + (list_box_coordinate.right - list_box_coordinate.left) / 2
        y = list_box_coordinate.top + (list_box_coordinate.bottom - list_box_coordinate.top) / 2

        return x, y

    @classmethod
    def get_accounts_info(cls):
        def get_name_widget(widget):
            return widget.element_info.name

        elements = cls.get_list_box_children()

        name_with_widget = [get_name_widget(element) for element in elements if
                            get_name_widget(element).endswith('widget')]

        name_without_widget = [element[:element.find('_____')] for element in name_with_widget]

        clean_name_with_widget = [cls.clean_login(element) for element in name_with_widget]



        return name_without_widget

    @classmethod
    @commands.utils.wait_before(1)
    def get_all_accounts_info(cls):
        accounts_info = cls.get_accounts_info()

        x, y = cls.get_list_box_coordinate_center()

        accounts = set(accounts_info)

        first_item = accounts_info[0]
        last_item = accounts_info[-1]

        while True:
            pyautogui.click(x, y)
            pyautogui.scroll(-1000)
            accounts_info = cls.get_accounts_info()
            accounts = accounts.union(accounts_info)

            if accounts_info[-1] == last_item:
                break

            last_item = accounts_info[-1]

        while True:
            pyautogui.click(x, y)
            pyautogui.scroll(1000)
            accounts_info = cls.get_accounts_info()

            if accounts_info[0] == first_item:
                break

        return accounts

    def get_account_info(self, account_info):
        d = 2

    def execute(self):
        return list(map(self.get_account_info, self.get_accounts_info()))
