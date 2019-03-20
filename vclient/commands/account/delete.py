import pywinauto

import commands
import pywinauto




class AccountNotDelete(Exception):
    pass


class Delete(commands.Command):
    BUTTON_ACCOUNT_DELETE = 'УДАЛИТЬButton'
    OFFSET_FROM_BUTTON = 54

    def __init__(self, account_login):
        self._account_login = account_login

        super().__init__(account_login)

    def _get_coordinate_button(self, account_position):
        bottom = account_position.bottom
        right = account_position.right
        top = account_position.top

        x = right - self.OFFSET_FROM_BUTTON
        y = top + int((bottom - top)/2)

        return x, y

    def _get_coordinate_center(self, account_position):
        x, y = self._get_coordinate_button(account_position)

        x -= 160

        return x, y


    def _is_account_delete(self):
        try:
            commands.account.Get(self._account_login)
        except commands.account.AccountNotFound:
            return True

        return False

    def execute(self):
        for _ in range(6):
            account = commands.account.Get(self._account_login).execute()
            account_position = account.rectangle

            pywinauto.mouse.click(coords=self._get_coordinate_center(account_position))

            pywinauto.mouse.click(coords=self._get_coordinate_button(account_position))

            try:
                self.pane.child_window(title="УДАЛИТЬ", control_type="Button").wait('exists', timeout=5)
            except pywinauto.application.TimeoutError:
                continue

            self.pane[self.BUTTON_ACCOUNT_DELETE].click()

            if self._is_account_delete():
                return

        raise AccountNotDelete








