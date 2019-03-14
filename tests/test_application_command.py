from unittest import TestCase

from vclient import commands

from common import StopStatus, StartStatus, WorkerStatus, AuthStatus


class TestApplicationCommand(TestCase):
    @classmethod
    def setUpClass(cls):
        commands.application.Stop()
        commands.application.Reset()

    def test1_stop(self):
        result = commands.application.Stop()
        self.assertEqual(result.status, StopStatus.STOP)
        self.assertEqual(result.data, None)

    def test2_start(self):
        result = commands.application.Start()
        self.assertEqual(result.status, StartStatus.START)
        self.assertEqual(result.data, None)

        result = commands.application.Start()
        self.assertEqual(result.status, StartStatus.ERROR_ALREADY_START)
        self.assertEqual(result.data, None)

    def test3_get_status(self):
        result = commands.application.Status()
        self.assertEqual(result.status, WorkerStatus.NOT_AUTH)
        self.assertEqual(result.data, None)

    def test4_check_auth(self):
        result = commands.application.Auth('login', 'password')
        self.assertEqual(result.status, AuthStatus.ERROR_LOGIN_OR_PASSWORD_INCORRECT)
        self.assertEqual(result.data, None)

        result = commands.application.Auth('dm.matveev1996@yandex.ru', 'dm.matveev1996@yandex.ru')
        self.assertEqual(result.status, AuthStatus.AUTH)
        self.assertEqual(result.data, None)

        result = commands.application.Auth('login', 'password')
        self.assertEqual(result.status, AuthStatus.ERROR_ALREADY_AUTH)
        self.assertEqual(result.data, None)

    def test5_get_status(self):
        result = commands.application.Status()
        self.assertEqual(result.status, WorkerStatus.READY)
        self.assertEqual(result.data, None)

        commands.application.Stop()

        result = commands.application.Status()
        self.assertEqual(result.status, WorkerStatus.STOP)
        self.assertEqual(result.data, None)
