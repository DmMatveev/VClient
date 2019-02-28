import pywinauto

import commands


class Delete(commands.Command):
    BUTTON_ACCOUNT_DELETE = 'УДАЛИТЬButton'
    OFFSET_FROM_BUTTON = 54

    def __init__(self, account_login):
        self._check_parameters(account_login)
        super().__init__()

        self._account_login = account_login

    @staticmethod
    def _check_parameters(*parameters):
        for parameter in parameters:
            if not isinstance(parameter, str) and parameter == '':
                raise commands.InvalidParameters

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

    #TODO Все таки надо листать список, если будет много

    def execute(self):
        account = commands.account.Get(self._account_login).execute()
        account_position = account.rectangle

        while True:
            pywinauto.mouse.click(coords=self._get_coordinate_button(account_position))

            try:
                self.pane.child_window(title="УДАЛИТЬ", control_type="Button").wait('exists', timeout=5)
            except pywinauto.timings.TimeoutError:
                pywinauto.mouse.click(coords=self._get_coordinate_center(account_position))
                continue

            break

        while True:
            self.pane[self.BUTTON_ACCOUNT_DELETE].click()

            try:
                account = commands.account.Get(self._account_login).execute()
                account_position = account.rectangle
                pywinauto.mouse.click(coords=self._get_coordinate_center(account_position))
            except commands.account.AccountNotFound:
                return True


