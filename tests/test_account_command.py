from unittest import TestCase

from vclient import commands


class TestAccountCommand(TestCase):
    @classmethod
    def setUpClass(cls):
        commands.application.Stop()
        commands.application.Start()
        commands.account.Clean()

    def test1_check_invalid_parameters(self):
        with self.assertRaises(commands.InvalidParameters):
            commands.account.Add('', '0@a.ru', 'password')
            commands.account.Add('vk', '', 'password')
            commands.account.Add('vk', '0@a.ru', '')

            commands.account.Get('')

            commands.account.Delete('')

        with self.assertRaises(commands.account.AccountNotFound):
            commands.account.Delete('0@a.ru')

    def test2_add_account_without_proxy(self):
        commands.account.Add('vk', '1@a.ru', 'password')
        commands.account.Add('vk', '2@a.ru', 'password')

        self.assertEqual(len(commands.account.List().result), 2)

        commands.account.Add('vk', '3@a.ru', 'password')
        commands.account.Add('vk', '4@a.ru', 'password')

        self.assertEqual(len(commands.account.List().result), 4)

    def test3_add_account_with_proxy(self):
        commands.account.Add('vk', '1@a.ru', 'password')
        commands.account.Add('vk', '2@a.ru', 'password')

        self.assertEqual(len(commands.account.List().result), 2)

        commands.account.Add('vk', '3@a.ru', 'password')
        commands.account.Add('vk', '4@a.ru', 'password')

        self.assertEqual(len(commands.account.List().result), 4)

    def test4_delete_account(self):
        commands.account.Add('vk', '1@a.ru', 'password')
        commands.account.Add('vk', '2@a.ru', 'password')
        commands.account.Add('vk', '3@a.ru', 'password')
        commands.account.Add('vk', '4@a.ru', 'password')
        commands.account.Add('vk', '5@a.ru', 'password')
        commands.account.Add('vk', '6@a.ru', 'password')
        commands.account.Add('vk', '7@a.ru', 'password')
        commands.account.Add('vk', '8@a.ru', 'password')
        commands.account.Add('vk', '9@a.ru', 'password')
        commands.account.Add('vk', '10@a.ru', 'password')
        commands.account.Add('vk', '11@a.ru', 'password')
        commands.account.Add('vk', '12@a.ru', 'password')
        commands.account.Add('vk', '13@a.ru', 'password')
        commands.account.Add('vk', '14@a.ru', 'password')
        commands.account.Add('vk', '15@a.ru', 'password')
        commands.account.Add('vk', '16@a.ru', 'password')
        commands.account.Add('vk', '17@a.ru', 'password')
        commands.account.Add('vk', '18@a.ru', 'password')
        commands.account.Add('vk', '19@a.ru', 'password')
        commands.account.Add('vk', '20@a.ru', 'password')

        #result = commands.account.List().result
        #self.assertEqual(len(result), 0)