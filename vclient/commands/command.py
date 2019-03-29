import logging
import os
from typing import NamedTuple

import pywinauto
from commands import utils
from common.common import ResultMessage, CommandStatus
from pywinauto import WindowSpecification

log = logging.getLogger(__name__)


class Command:
    RPC = True

    app = pywinauto.Application(backend='uia')
    pane: WindowSpecification = None

    APP_DIR = f'{os.path.split(os.getenv("APPDATA"))[0]}\\Local\\VtopeBot'

    def __init__(self):
        while True:
            try:
                self.pane.child_window(title="backgroundModalWidget", control_type="Custom").wait_not('exists',
                                                                                                      timeout=1)
            except AttributeError:
                break

            except RuntimeError:
                log.error('Close backgroundModalWidget')
                utils.wait(3)

                try:
                    self.pane.child_window(control_type='Button', ctrl_index=-1).click()

                except pywinauto.findwindows.ElementNotFoundError as e:
                    log.exception(e)

                except pywinauto.findwindows.ElementAmbiguousError as e:
                    log.exception(e)

                except Exception as e:
                    log.exception(e)

            except Exception as e:
                log.exception(e)

            break

        try:
            self.pane.child_window(title="скрыть совет", control_type="Button").click()

        except AttributeError:
            pass

        except pywinauto.findwindows.ElementNotFoundError as e:
            pass

        except pywinauto.findwindows.ElementAmbiguousError as e:
            pass

        except Exception as e:
            log.exception(e)

        try:
            result = self.execute()

        except Exception as e:
            result = CommandStatus.ERROR

            log.exception(e)

            try:
                self.error_handler()
            except Exception as e:
                log.exception(e)

        else:
            try:
                if self.is_error():
                    result = CommandStatus.ERROR

                    try:
                        self.error_handler()
                    except Exception as e:
                        log.exception(e)

            except Exception as e:
                log.exception(e)
                result = CommandStatus.ERROR

        try:
            self._status, self._data = result
        except TypeError:
            self._status = result
            self._data = None

    def execute(self):  # написать вовзврат двух аргументов
        raise NotImplementedError

    def error_handler(self):
        pass

    def is_error(self):
        return False

    @property
    def status(self) -> CommandStatus:
        return self._status

    @property
    def data(self) -> NamedTuple:
        return self._data

    @property
    def message(self):
        return ResultMessage(self._status, self._data)
