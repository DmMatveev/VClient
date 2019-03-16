from enum import Enum

import commands


class Switch(commands.Command):
    LAYER_IS_ACCOUNT = True

    BUTTON_SWITCH_TO_PROXY = 'Button11'
    BUTTON_SWITCH_TO_ACCOUNT = 'Button8'

    def execute(self):
        if self.LAYER_IS_ACCOUNT:
            self.pane[self.BUTTON_SWITCH_TO_ACCOUNT].click()
        else:
            self.pane[self.BUTTON_SWITCH_TO_PROXY].click()

        return None
