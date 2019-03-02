import os
import subprocess

import pywinauto
from pywinauto import Application

'''
Вызов любых методов, если приложение работает
авторизоваться
проверка чтоб был на экране и не минизирован
'''

class Window:
    FILE_DELETE = ['accs.data', 'vdata', 'backup', 'snproxy', 'vproxy']

    INPUT_LOGIN = 'Edit1'
    INPUT_PASSWORD = 'Edit2'
    BUTTON_AUTH = 'Button3'
    PATH_START = 'C:\\Users\\Dmitry\\AppData\\Local\\VtopeBot\\vtopebot.exe'
    PATH_STOP = 'C:\\Users\\Dmitry\\AppData\\Local\\VtopeBot\\killprocesses.bat'

    def __init__(self):
        self._app = Application(backend='uia')
        self.start_process()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.stop_process()

    def start_process(self):
        try:
            self._app.connect(path=self.PATH_START)
        except pywinauto.application.ProcessNotFoundError:
            self.stop_process()
            subprocess.Popen(self.PATH_START, cwd=os.path.dirname(self.PATH_START))
            self._app.connect(path=self.PATH_START, timeout=10)

        return self.is_process_running()

    def stop_process(self):
        subprocess.call(self.PATH_STOP, cwd=os.path.dirname(self.PATH_STOP), stdout=None)

    def reboot_process(self):
        if self.is_process_running():
            self.stop_process()
            return self.start_process()

        return self.start_process()

    def is_process_running(self):
        return self._app.is_process_running()

    def is_auth(self):
        try:
            self._app.Pane.child_window(title="Логин втопе", control_type="Text").wait('exists', timeout=5)
        except pywinauto.timings.TimeoutError:
            return True

        return False

    def auth(self, login, password):
        pane = self.get_main_pane()

        pane[self.INPUT_LOGIN].set_text(login)
        pane[self.INPUT_PASSWORD].set_text(password)
        pane[self.BUTTON_AUTH].click()

        # 5 * 6 = 30 секунд ожидание авторизации
        if any([self.is_auth()]*6):
            return True

        try:
            self._app.Pane[self.TEXT_ERROR_AUTH].wait('exists', timeout=3)
        except pywinauto.timings.TimeoutError:
            pass
        else:
            raise ExceptionAuth('')

        try:
            self._app.Pane[self.TEXT_ERROR_NO_INTERNET].wait('exists', timeout=3)
        except pywinauto.timings.TimeoutError:
            pass
        else:
            raise ExceptionInternet

        return False

    def reset_program(self):
        self.stop_process()
        program_path = os.path.dirname(self.PATH_START)
        files = os.listdir(program_path)

        for file in files:
            if any(map(file.endswith, self.FILE_DELETE)):
                path = os.path.join(program_path, file)
                os.remove(path)

    def is_ready(self):
        pass

    def get_main_pane(self):
        return self._app.Pane
