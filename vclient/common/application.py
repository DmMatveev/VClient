from enum import Enum
from typing import NamedTuple


class ApplicationAuthParameters(NamedTuple):
    login: str
    password: str


class ApplicationWorkerStatus(Enum):
    NOT_AUTH = 'Vtope bot не авторизован'
    READY = 'Vtope bot готов к работе'
    STOP = 'Vtope bot закрыт'
    WORK = 'Vtope bot работает'


class StartStatus(Enum):
    ERROR_ALREADY_START = 'Ошибка. Vtope bot уже запущен'
    ERROR = 'Неизвестная ошибка'
    START = 'Vtope bot запущен'


class StopStatus(Enum):
    ERROR = 'Неизвестная ошибка'
    STOP = 'Vtope bot закрыт'
