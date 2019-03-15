from unittest import TestCase

import commands
from common.proxy import ProxyAddParameters, ProxyType


class TestProxy(TestCase):
    @classmethod
    def setUpClass(cls):
        commands.application.Start()

    def test1_add_proxy(self):
        for i in range(5):
            parameters = ProxyAddParameters(f'{i}{i}', 50, ProxyType.HTTPS, 'login', 'password')
            result = commands.proxy.Add(parameters)
            #self.assertEqual(result.status, AccountAddStatus.ADD)
            #self.assertEqual(result.data, None)
