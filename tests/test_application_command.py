import unittest

import commands
from common.application import ApplicationStatus, ApplicationAuthParameters
from common.common import CommandStatus


class TestApplicationCommand(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        #commands.application.Stop()
        commands.application.Start()

    def test1_stop(self):
        result = commands.application.Stop()
        self.assertEqual(result.status, CommandStatus.SUCCESS)
        self.assertEqual(result.data, None)

    def test2_status(self):
        result = commands.application.Status()
        self.assertEqual(result.status, CommandStatus.SUCCESS)
        self.assertEqual(result.data, ApplicationStatus.STOP)

    def test3_start(self):
        result = commands.application.Start()
        self.assertEqual(result.status, CommandStatus.SUCCESS)
        self.assertEqual(result.data, None)

        result = commands.application.Start()
        self.assertEqual(result.status, CommandStatus.ERROR)
        self.assertEqual(result.data, None)

    def test4_status(self):
        result = commands.application.Status()
        self.assertEqual(result.status, CommandStatus.SUCCESS)
        self.assertEqual(result.data, ApplicationStatus.NOT_AUTH)

    def test5_auth(self):
        parameters = ApplicationAuthParameters('login', 'password')
        result = commands.application.Auth(parameters)
        self.assertEqual(result.status, CommandStatus.SUCCESS)
        self.assertEqual(result.data, None)

    @unittest.skip
    def test6_status(self):
        result = commands.application.Status()
        self.assertEqual(result.status, CommandStatus.SUCCESS)
        self.assertEqual(result.data, ApplicationStatus.AUTH_LOGIN_OR_PASSWORD_INCORRECT)

    def test7_auth(self):
        parameters = ApplicationAuthParameters('dm.matveev1996@yandex.ru', 'dm.matveev1996@yandex.ru')
        result = commands.application.Auth(parameters)
        self.assertEqual(result.status, CommandStatus.SUCCESS)
        self.assertEqual(result.data, None)

    def test8_status(self):
        result = commands.application.Status()
        self.assertEqual(result.status, CommandStatus.SUCCESS)
        self.assertEqual(result.data, ApplicationStatus.READY)

    def test9_auth(self):
        parameters = ApplicationAuthParameters('login', 'password')
        result = commands.application.Auth(parameters)
        self.assertEqual(result.status, CommandStatus.ERROR)
        self.assertEqual(result.data, None)
