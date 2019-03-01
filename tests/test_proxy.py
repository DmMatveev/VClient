from unittest import TestCase

from pywinauto import Application

from src import commands


class TestProxy(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.app = Application(backend='uia').connect(path="C:\\Users\\Dmitry\\AppData\\Local\\VtopeBot\\vtopebot.exe")
        cls.app = cls.app.Pane
        commands.Command.pane = cls.app
        #commands.prox.Clean().execute()

    def test1_check_invalid_parameters(self):
        with self.assertRaises(src.commands.account.InvalidParameters):
            src.commands.account.Add('', '0@a.ru', 'password').execute()
            src.commands.account.Add('vk', '', 'password').execute()
            src.commands.account.Add('vk', '0@a.ru', '').execute()

            src.commands.account.Get('').execute()

            src.commands.account.Delete('').execute()

        with self.assertRaises(src.commands.account.AccountNotFound):
            src.commands.account.Delete('0@a.ru').execute()

    def test2_add_proxy(self):
        src.commands.account.Add('vk', '1@a.ru', 'password').execute()
        src.commands.account.Add('vk', '2@a.ru', 'password').execute()

        self.assertEqual(len(src.commands.account.List().execute()), 2)

        src.commands.account.Add('vk', '3@a.ru', 'password').execute()
        src.commands.account.Add('vk', '4@a.ru', 'password').execute()

        self.assertEqual(len(src.commands.account.List().execute()), 4)
