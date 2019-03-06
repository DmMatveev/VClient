from unittest import TestCase

from vclient import commands


class TestApplicationCommand(TestCase):
    @classmethod
    def setUpClass(cls):
        commands.application.Stop()
        commands.application.Reset()

    def test1_get_status(self):
        result = commands.application.Status().result
        self.assertEqual(result, 'STOP')

        result = commands.application.Start().result
        self.assertEqual(result, 'START_SUCCESS')

        result = commands.application.Status().result
        self.assertEqual(result, 'NOT_AUTH')

    def test2_check_auth(self):
        result = commands.application.Auth('login', 'password').result
        self.assertEqual(result, 'ERROR_LOGIN_OR_PASSWORD_INCORRECT')

        result = commands.application.Auth('dm.matveev1996@yandex.ru', 'dm.matveev1996@yandex.ru').result
        self.assertEqual(result, 'SUCCESS')

        result = commands.application.Auth('login', 'password').result
        self.assertEqual(result, 'ERROR_ALREADY_AUTH')

    def test3_get_status(self):
        result = commands.application.Status().result
        self.assertEqual(result, 'READY')
