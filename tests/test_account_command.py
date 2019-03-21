import time
from unittest import TestCase

from common.account import AccountAddParameters, AccountType, AccountAddStatus
import commands
from common.common import CommandStatus


class TestAccountCommand(TestCase):
    @classmethod
    def setUpClass(cls):
        commands.application.Start()

    def test1_add_with_error(self):
        parameters = AccountAddParameters(f'1@a.ru', '', AccountType.INSTAGRAM)
        result = commands.account.Add(parameters)
        self.assertEqual(result.status, CommandStatus.ERROR)
        self.assertEqual(result.data, None)

        parameters = AccountAddParameters(f'', 'password', AccountType.INSTAGRAM)
        result = commands.account.Add(parameters)
        self.assertEqual(result.status, CommandStatus.ERROR)
        self.assertEqual(result.data, None)

    def test2_add_account_without_proxy(self):
        parameters = AccountAddParameters(f'-1@a.ru', 'password', AccountType.INSTAGRAM)
        result = commands.account.Add(parameters)
        self.assertEqual(result.status, CommandStatus.SUCCESS)
        self.assertEqual(result.data, None)

        parameters = AccountAddParameters(f'-2@a.ru', 'password', AccountType.INSTAGRAM)
        result = commands.account.Add(parameters)
        self.assertEqual(result.status, CommandStatus.SUCCESS)
        self.assertEqual(result.data, None)

        parameters = AccountAddParameters(f'-3@a.ru', 'password', AccountType.INSTAGRAM)
        result = commands.account.Add(parameters)
        self.assertEqual(result.status, CommandStatus.SUCCESS)
        self.assertEqual(result.data, None)

    def test3_add_account_with_proxy(self):
            parameters = AccountAddParameters(f'1@a.ru', 'password', AccountType.INSTAGRAM, proxy=f'127.0.0.1')

            result = commands.account.Add(parameters)
            self.assertEqual(result.status, CommandStatus.SUCCESS)
            self.assertEqual(result.data, None)

            parameters = AccountAddParameters(f'', 'password', AccountType.INSTAGRAM, proxy=f'127.0.0.2')
            result = commands.account.Add(parameters)
            self.assertEqual(result.status, CommandStatus.ERROR)
            self.assertEqual(result.data, None)

            parameters = AccountAddParameters(f'2@a.ru', 'password', AccountType.INSTAGRAM, proxy=f'127.0.0.2')
            result = commands.account.Add(parameters)
            self.assertEqual(result.status, CommandStatus.SUCCESS)
            self.assertEqual(result.data, None)

            parameters = AccountAddParameters(f'3@a.ru', 'password', AccountType.INSTAGRAM, proxy=f'127.0.0.3')
            result = commands.account.Add(parameters)
            self.assertEqual(result.status, CommandStatus.SUCCESS)
            self.assertEqual(result.data, None)

            parameters = AccountAddParameters(f'4@a.ru', 'password', AccountType.INSTAGRAM, proxy=f'127.0.0.4')
            result = commands.account.Add(parameters)
            self.assertEqual(result.status, CommandStatus.SUCCESS)
            self.assertEqual(result.data, None)

            parameters = AccountAddParameters(f'5@a.ru', 'password', AccountType.INSTAGRAM, proxy=f'127.0.0.5')
            result = commands.account.Add(parameters)
            self.assertEqual(result.status, CommandStatus.SUCCESS)
            self.assertEqual(result.data, None)

            parameters = AccountAddParameters(f'6@a.ru', 'password', AccountType.INSTAGRAM, proxy=f'127.0.0.6')
            result = commands.account.Add(parameters)
            self.assertEqual(result.status, CommandStatus.SUCCESS)
            self.assertEqual(result.data, None)

            parameters = AccountAddParameters(f'7@a.ru', 'password', AccountType.INSTAGRAM, proxy=f'127.0.0.7')
            result = commands.account.Add(parameters)
            self.assertEqual(result.status, CommandStatus.SUCCESS)
            self.assertEqual(result.data, None)

            parameters = AccountAddParameters(f'7@a.ru', '', AccountType.INSTAGRAM, proxy=f'127.0.0.7')
            result = commands.account.Add(parameters)
            self.assertEqual(result.status, CommandStatus.ERROR)
            self.assertEqual(result.data, None)

            parameters = AccountAddParameters(f'8@a.ru', 'password', AccountType.INSTAGRAM, proxy=f'127.0.0.8')
            result = commands.account.Add(parameters)
            self.assertEqual(result.status, CommandStatus.SUCCESS)
            self.assertEqual(result.data, None)

            parameters = AccountAddParameters(f'9@a.ru', 'password', AccountType.INSTAGRAM, proxy=f'127.0.0.9')
            result = commands.account.Add(parameters)
            self.assertEqual(result.status, CommandStatus.SUCCESS)
            self.assertEqual(result.data, None)

            parameters = AccountAddParameters(f'10@a.ru', 'password', AccountType.INSTAGRAM, proxy=f'127.0.0.10')
            result = commands.account.Add(parameters)
            self.assertEqual(result.status, CommandStatus.SUCCESS)
            self.assertEqual(result.data, None)

    def test4_list(self):
        result = commands.account.List()
        self.assertEqual(result.status, CommandStatus.SUCCESS)
        self.assertEqual(len(result.data), 10)
