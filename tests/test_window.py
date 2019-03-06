from unittest import TestCase

from vclient.main import application


class TestWindow(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.window = application.Window()
        cls.window.reset_program()
        cls.window.start_process()

    def test1_close_program(self):
        self.window.stop_process()
        self.assertFalse(self.window.is_process_running())

    def test2_start_program(self):
        self.window.start_process()
        self.assertTrue(self.window.is_process_running())

    def test3_reboot_program(self):
        self.window.reboot_process()
        self.assertTrue(self.window.is_process_running())

        self.window.stop_process()
        self.window.reboot_process()
        self.assertTrue(self.window.is_process_running())

    def test4_auth(self):
        self.assertRaises(application.ExceptionAuth, self.window.auth('123', '123'))
        self.assertTrue(self.window.auth('dm.matveev1996@yandex.ru', 'E11rr12or96'))

    def test5_reset_program(self):
        self.window.reset_program()
        self.window.start_process()
        self.assertFalse(self.window.is_not_auth())

    def test6_check_minimize(self):
        pass
