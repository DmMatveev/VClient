import unittest

import commands
from common.common import CommandStatus
from common.proxy import ProxyAddParameters, ProxyType, ProxyDeleteParameters


class TestProxy(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        commands.application.Start()

    def test1_add_with_error(self):
        parameters = ProxyAddParameters('', 1000, ProxyType.HTTPS, 'login', 'password')
        result = commands.proxy.Add(parameters)
        self.assertEqual(result.status, CommandStatus.ERROR)
        self.assertEqual(result.data, None)

    def test2_add(self):
        parameters = ProxyAddParameters('127.0.0.1', 1001, ProxyType.HTTPS, 'login', 'password')
        result = commands.proxy.Add(parameters)
        self.assertEqual(result.status, CommandStatus.SUCCESS)
        self.assertEqual(result.data, None)

        parameters = ProxyAddParameters('127.0.0.2', 'port', ProxyType.HTTPS, 'login', 'password')
        result = commands.proxy.Add(parameters)
        self.assertEqual(result.status, CommandStatus.ERROR)
        self.assertEqual(result.data, None)

        parameters = ProxyAddParameters('127.0.0.2', 1002, ProxyType.HTTPS, 'login', 'password')
        result = commands.proxy.Add(parameters)
        self.assertEqual(result.status, CommandStatus.SUCCESS)
        self.assertEqual(result.data, None)

        parameters = ProxyAddParameters('127.0.0.3', 1003, ProxyType.HTTPS, 'login', 'password')
        result = commands.proxy.Add(parameters)
        self.assertEqual(result.status, CommandStatus.SUCCESS)
        self.assertEqual(result.data, None)

        parameters = ProxyAddParameters('', 1004, ProxyType.HTTPS, 'login', 'password')
        result = commands.proxy.Add(parameters)
        self.assertEqual(result.status, CommandStatus.ERROR)
        self.assertEqual(result.data, None)

        parameters = ProxyAddParameters('127.0.0.4', 1004, ProxyType.HTTPS, 'login', 'password')
        result = commands.proxy.Add(parameters)
        self.assertEqual(result.status, CommandStatus.SUCCESS)
        self.assertEqual(result.data, None)

        parameters = ProxyAddParameters('127.0.0.5', 1005, ProxyType.HTTPS, 'login', 'password')
        result = commands.proxy.Add(parameters)
        self.assertEqual(result.status, CommandStatus.SUCCESS)
        self.assertEqual(result.data, None)

        parameters = ProxyAddParameters('127.0.0.6', 1006, ProxyType.HTTPS, 'login', 'password')
        result = commands.proxy.Add(parameters)
        self.assertEqual(result.status, CommandStatus.SUCCESS)
        self.assertEqual(result.data, None)

        parameters = ProxyAddParameters('127.0.0.7', 1007, ProxyType.HTTPS, 'login', 'password')
        result = commands.proxy.Add(parameters)
        self.assertEqual(result.status, CommandStatus.SUCCESS)
        self.assertEqual(result.data, None)

        parameters = ProxyAddParameters('127.0.0.8', 1008, ProxyType.HTTPS, 'login', 'password')
        result = commands.proxy.Add(parameters)
        self.assertEqual(result.status, CommandStatus.SUCCESS)
        self.assertEqual(result.data, None)

        parameters = ProxyAddParameters('', 'port', ProxyType.HTTPS, 'login', 'password')
        result = commands.proxy.Add(parameters)
        self.assertEqual(result.status, CommandStatus.ERROR)
        self.assertEqual(result.data, None)

        parameters = ProxyAddParameters('', 'port', ProxyType.HTTPS, 'login', 'password')
        result = commands.proxy.Add(parameters)
        self.assertEqual(result.status, CommandStatus.ERROR)
        self.assertEqual(result.data, None)

        parameters = ProxyAddParameters('127.0.0.9', 1009, ProxyType.HTTPS, 'login', 'password')
        result = commands.proxy.Add(parameters)
        self.assertEqual(result.status, CommandStatus.SUCCESS)
        self.assertEqual(result.data, None)

        parameters = ProxyAddParameters('127.0.0.10', 1010, ProxyType.HTTPS, 'login', 'password')
        result = commands.proxy.Add(parameters)
        self.assertEqual(result.status, CommandStatus.SUCCESS)
        self.assertEqual(result.data, None)

    def test3_list(self):
        result = commands.proxy.List()
        self.assertEqual(result.status, CommandStatus.SUCCESS)
        self.assertEqual(len(result.data), 10)

    def test4_delete(self):
        parameters = ProxyDeleteParameters('127.0.0.0')
        result = commands.proxy.Delete(parameters)
        self.assertEqual(result.status, CommandStatus.ERROR)
        self.assertEqual(result.data, None)

        parameters = ProxyDeleteParameters('127.0.0.1')
        result = commands.proxy.Delete(parameters)
        self.assertEqual(result.status, CommandStatus.SUCCESS)
        self.assertEqual(result.data, None)

        parameters = ProxyDeleteParameters('127.0.0.2')
        result = commands.proxy.Delete(parameters)
        self.assertEqual(result.status, CommandStatus.SUCCESS)
        self.assertEqual(result.data, None)

        parameters = ProxyDeleteParameters('127.0.0.3')
        result = commands.proxy.Delete(parameters)
        self.assertEqual(result.status, CommandStatus.SUCCESS)
        self.assertEqual(result.data, None)

        parameters = ProxyDeleteParameters('127.0.0.4')
        result = commands.proxy.Delete(parameters)
        self.assertEqual(result.status, CommandStatus.SUCCESS)
        self.assertEqual(result.data, None)

        parameters = ProxyDeleteParameters('127.0.0.5')
        result = commands.proxy.Delete(parameters)
        self.assertEqual(result.status, CommandStatus.SUCCESS)
        self.assertEqual(result.data, None)

        parameters = ProxyDeleteParameters('127.0.0.5')
        result = commands.proxy.Delete(parameters)
        self.assertEqual(result.status, CommandStatus.ERROR)
        self.assertEqual(result.data, None)

        parameters = ProxyDeleteParameters('127.0.0.6')
        result = commands.proxy.Delete(parameters)
        self.assertEqual(result.status, CommandStatus.SUCCESS)
        self.assertEqual(result.data, None)

    def test5_list(self):
        result = commands.proxy.List()
        self.assertEqual(result.status, CommandStatus.SUCCESS)
        self.assertEqual(len(result.data), 4)
