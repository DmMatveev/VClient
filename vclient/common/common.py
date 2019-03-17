from enum import Enum, auto
from typing import NamedTuple


class CommandMessage(NamedTuple):
    command: str
    parameters: NamedTuple = None


class ResultMessage(NamedTuple):
    status: Enum
    data: Enum = None




class AuthStatus(Enum):
    ERROR_LOGIN_OR_PASSWORD_INCORRECT = 'Ошибка. Логин или пароль неверны'
    ERROR_SERVER_NOT_RESPONSE = 'Ошибка. Сервер не отвечает'
    ERROR_ALREADY_AUTH = 'Ошибка. Vtope bot уже авторизован'
    ERROR = 'Неизвестная ошибка'
    AUTH = 'Авторизация прошла успешна'


class ResetStatus(Enum):
    ERROR_APP_START = auto()
    ERROR = auto()
    RESET = auto()
