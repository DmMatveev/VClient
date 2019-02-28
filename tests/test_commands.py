from unittest import TestCase

from pywinauto import Application

import commands


class TestAddAccount(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.app = Application(backend='uia').connect(path="C:\\Users\\Dmitry\\AppData\\Local\\VtopeBot\\vtopebot.exe")
        cls.app = cls.app.Pane
        commands.Command.pane = cls.app
        commands.account.Clean().execute()

    def test1_check_invalid_parameters(self):
        with self.assertRaises(commands.account.InvalidParameters):
            commands.account.Add('', '0@a.ru', 'password').execute()
            commands.account.Add('vk', '', 'password').execute()
            commands.account.Add('vk', '0@a.ru', '').execute()

            commands.account.Get('').execute()

            commands.account.Delete('').execute()

        with self.assertRaises(commands.account.AccountNotFound):
            commands.account.Delete('0@a.ru').execute()

    def test2_add_account_without_proxy(self):
        commands.account.Add('vk', '1@a.ru', 'password').execute()
        commands.account.Add('vk', '2@a.ru', 'password').execute()

        self.assertEqual(len(commands.account.List().execute()), 2)

        commands.account.Add('vk', '3@a.ru', 'password').execute()
        commands.account.Add('vk', '4@a.ru', 'password').execute()

        self.assertEqual(len(commands.account.List().execute()), 4)

    def test3_add_account_with_proxy(self):
        pass

    def test4_delete_account(self):
        commands.account.Add('vk', '5@a.ru', 'password').execute()

        self.assertEqual(len(commands.account.List().execute()), 5)

        commands.account.Delete('1@a.ru').execute()
        commands.account.Delete('3@a.ru').execute()

        result = commands.account.List().execute()
        self.assertEqual(len(result), 3)

        self.assertEqual(result[0]['login'], '2@a.ru')
        self.assertEqual(result[1]['login'], '4@a.ru')
        self.assertEqual(result[2]['login'], '5@a.ru')

        commands.account.Add('vk', '6@a.ru', 'password').execute()
        commands.account.Add('vk', '7@a.ru', 'password').execute()
        commands.account.Add('vk', '8@a.ru', 'password').execute()

        self.assertEqual(len(commands.List().execute()), 6)

        commands.account.Delete('7@a.ru').execute()
        commands.account.Delete('2@a.ru').execute()
        commands.account.Delete('5@a.ru').execute()
        commands.account.Delete('8@a.ru').execute()

        result = commands.account.List().execute()
        self.assertEqual(len(result), 2)

        self.assertEqual(result[0]['login'], '4@a.ru')
        self.assertEqual(result[1]['login'], '6@a.ru')

        commands.account.Delete('6@a.ru').execute()
        commands.account.Delete('4@a.ru').execute()

        result = commands.account.List().execute()
        self.assertEqual(len(result), 0)

    def _test5_scroll_list_and_delete(self):
        commands.account.Add('vk', '1@a.ru', 'password').execute()
        commands.account.Add('vk', '2@a.ru', 'password').execute()
        commands.account.Add('vk', '3@a.ru', 'password').execute()
        commands.account.Add('vk', '4@a.ru', 'password').execute()
        commands.account.Add('vk', '5@a.ru', 'password').execute()
        commands.account.Add('vk', '6@a.ru', 'password').execute()
        commands.account.Add('vk', '7@a.ru', 'password').execute()
        commands.account.Add('vk', '8@a.ru', 'password').execute()
        commands.account.Add('vk', '9@a.ru', 'password').execute()
        commands.account.Add('vk', '10@a.ru', 'password').execute()
        commands.account.Add('vk', '11@a.ru', 'password').execute()
        commands.account.Add('vk', '12@a.ru', 'password').execute()
        commands.account.Add('vk', '13@a.ru', 'password').execute()
        commands.account.Add('vk', '14@a.ru', 'password').execute()
        commands.account.Add('vk', '15@a.ru', 'password').execute()
        commands.account.Add('vk', '16@a.ru', 'password').execute()
        commands.account.Add('vk', '17@a.ru', 'password').execute()
        commands.account.Add('vk', '18@a.ru', 'password').execute()
        commands.account.Add('vk', '19@a.ru', 'password').execute()
        commands.account.Add('vk', '20@a.ru', 'password').execute()

        self.assertEqual(len(commands.account.List().execute()), 20)
