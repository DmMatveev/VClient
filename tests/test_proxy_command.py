from unittest import TestCase

from vclient import commands

import time


class TestProxy(TestCase):
    @classmethod
    def setUpClass(cls):
        commands.application.Stop().execute()
        commands.application.Start().execute()
        time.sleep(5)
        commands.Command.app.print_control_identifiers(depth=1000)

    def test1_check_invalid_parameters(self):
        pass

    def test2_add_proxy(self):
        pass