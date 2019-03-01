from unittest import TestCase

from pywinauto import Application

from src import commands


class TestA(TestCase):
    def test_A(self):
        app = Application(backend='uia').connect(path="C:\\Users\\Dmitry\\AppData\\Local\\VtopeBot\\vtopebot.exe")
        app = app.Pane
        app.print_control_identifiers(depth=1000)


class TestAddAccount(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.app = Application(backend='uia').connect(path="C:\\Users\\Dmitry\\AppData\\Local\\VtopeBot\\vtopebot.exe")
        cls.app = cls.app.Pane
        commands.Command.pane = cls.app
        cls.app.print_control_identifiers(depth=1000)
        src.commands.account.Clean().execute()

    def test1_check_invalid_parameters(self):
        with self.assertRaises(src.commands.account.InvalidParameters):
            src.commands.account.Add('', '0@a.ru', 'password').execute()
            src.commands.account.Add('vk', '', 'password').execute()
            src.commands.account.Add('vk', '0@a.ru', '').execute()

            src.commands.account.Get('').execute()

            src.commands.account.Delete('').execute()

        with self.assertRaises(src.commands.account.AccountNotFound):
            src.commands.account.Delete('0@a.ru').execute()

    def test2_add_account_without_proxy(self):
        src.commands.account.Add('vk', '1@a.ru', 'password').execute()
        src.commands.account.Add('vk', '2@a.ru', 'password').execute()

        self.assertEqual(len(src.commands.account.List().execute()), 2)

        src.commands.account.Add('vk', '3@a.ru', 'password').execute()
        src.commands.account.Add('vk', '4@a.ru', 'password').execute()

        self.assertEqual(len(src.commands.account.List().execute()), 4)

    def test3_add_account_with_proxy(self):
        pass

    def test4_delete_account(self):
        src.commands.account.Add('vk', '5@a.ru', 'password').execute()

        self.assertEqual(len(src.commands.account.List().execute()), 5)

        src.commands.account.Delete('1@a.ru').execute()
        src.commands.account.Delete('3@a.ru').execute()

        result = src.commands.account.List().execute()
        self.assertEqual(len(result), 3)

        self.assertEqual(result[0]['login'], '2@a.ru')
        self.assertEqual(result[1]['login'], '4@a.ru')
        self.assertEqual(result[2]['login'], '5@a.ru')

        src.commands.account.Add('vk', '6@a.ru', 'password').execute()
        src.commands.account.Add('vk', '7@a.ru', 'password').execute()
        src.commands.account.Add('vk', '8@a.ru', 'password').execute()

        self.assertEqual(len(commands.List().execute()), 6)

        src.commands.account.Delete('7@a.ru').execute()
        src.commands.account.Delete('2@a.ru').execute()
        src.commands.account.Delete('5@a.ru').execute()
        src.commands.account.Delete('8@a.ru').execute()

        result = src.commands.account.List().execute()
        self.assertEqual(len(result), 2)

        self.assertEqual(result[0]['login'], '4@a.ru')
        self.assertEqual(result[1]['login'], '6@a.ru')

        src.commands.account.Delete('6@a.ru').execute()
        src.commands.account.Delete('4@a.ru').execute()

        result = src.commands.account.List().execute()
        self.assertEqual(len(result), 0)

    def _test5_scroll_list_and_delete(self):
        src.commands.account.Add('vk', '1@a.ru', 'password').execute()
        src.commands.account.Add('vk', '2@a.ru', 'password').execute()
        src.commands.account.Add('vk', '3@a.ru', 'password').execute()
        src.commands.account.Add('vk', '4@a.ru', 'password').execute()
        src.commands.account.Add('vk', '5@a.ru', 'password').execute()
        src.commands.account.Add('vk', '6@a.ru', 'password').execute()
        src.commands.account.Add('vk', '7@a.ru', 'password').execute()
        src.commands.account.Add('vk', '8@a.ru', 'password').execute()
        src.commands.account.Add('vk', '9@a.ru', 'password').execute()
        src.commands.account.Add('vk', '10@a.ru', 'password').execute()
        src.commands.account.Add('vk', '11@a.ru', 'password').execute()
        src.commands.account.Add('vk', '12@a.ru', 'password').execute()
        src.commands.account.Add('vk', '13@a.ru', 'password').execute()
        src.commands.account.Add('vk', '14@a.ru', 'password').execute()
        src.commands.account.Add('vk', '15@a.ru', 'password').execute()
        src.commands.account.Add('vk', '16@a.ru', 'password').execute()
        src.commands.account.Add('vk', '17@a.ru', 'password').execute()
        src.commands.account.Add('vk', '18@a.ru', 'password').execute()
        src.commands.account.Add('vk', '19@a.ru', 'password').execute()
        src.commands.account.Add('vk', '20@a.ru', 'password').execute()

        self.assertEqual(len(src.commands.account.List().execute()), 20)
