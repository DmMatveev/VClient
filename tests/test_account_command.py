from unittest import TestCase

from common.account import AccountAddParameters, AccountType, AccountAddStatus
import commands


class TestAccountCommand(TestCase):
    @classmethod
    def setUpClass(cls):
        commands.application.Start()

    def test1_add_account_without_proxy(self):
        for i in range(5):
            parameters = AccountAddParameters(f'{i}@a.ru', 'password', AccountType.INSTAGRAM)
            result = commands.account.Add(parameters)
            self.assertEqual(result.status, AccountAddStatus.ADD)
            self.assertEqual(result.data, None)

    def test2_add_account_with_proxy(self):
        for i in range(5, 10):
            parameters = AccountAddParameters(f'{i}@a.ru', 'password', AccountType.INSTAGRAM, proxy=f'{i - 10}')
            result = commands.account.Add(parameters)
            self.assertEqual(result.status, AccountAddStatus.ADD)
            self.assertEqual(result.data, None)
