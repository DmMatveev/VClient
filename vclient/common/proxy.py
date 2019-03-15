from enum import Enum, auto
from typing import NamedTuple


class ProxyType(Enum):
    HTTP = auto()
    HTTPS = auto()
    SOCKS5 = auto()


class ProxyAddParameters(NamedTuple):
    ip: str
    port: int
    type: ProxyType
    login: str = ''
    password: str = ''


class ProxyAddStatus(Enum):
    ERROR_NOT_ADD = 'Ошибка. Прокси не добавлен',
    ERROR = 'Неизвестная ошибка'
    ADD = 'Прокси успешно добавлен'
