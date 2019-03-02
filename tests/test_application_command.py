from unittest import TestCase

from vclient import commands


class TestApplicationCommand(TestCase):
    @classmethod
    def setUpClass(cls):
        commands.application.Stop()
        commands.application.Reset()
        commands.application.Start()

    def test1_check_auth(self):
        with self.assertRaises(commands.application.LoginOrPasswordIncorrect):
            commands.application.Auth('login', 'password')

        commands.application.Auth('dm.matveev1996@yandex.ru', 'dm.matveev1996@yandex.ru')

        with self.assertRaises(commands.application.AppAlreadyAuth):
            commands.application.Auth('login', 'password')

    def test2_check_stop(self):
        commands.application.Stop()
