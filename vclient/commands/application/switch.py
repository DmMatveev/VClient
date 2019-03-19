import commands
from commands import utils


class Switch(commands.Command):
    LAYER_IS_ACCOUNT = True

    BUTTON_SWITCH_TO_PROXY = 'Button11'
    BUTTON_SWITCH_TO_ACCOUNT = 'Button8'

    @classmethod
    @utils.wait_after(1)
    def switch_to_account(cls):
        if cls.LAYER_IS_ACCOUNT:
            return

        cls.pane[cls.BUTTON_SWITCH_TO_ACCOUNT].click()
        cls.LAYER_IS_ACCOUNT = True

    @classmethod
    @utils.wait_after(1)
    def switch_to_proxy(cls):
        if cls.LAYER_IS_ACCOUNT:
            cls.pane[cls.BUTTON_SWITCH_TO_PROXY].click()
            cls.LAYER_IS_ACCOUNT = False

    def execute(self):
        return None
