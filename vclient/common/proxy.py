from enum import Enum, auto
from typing import NamedTuple


class ProxyType(Enum):
    HTTP = auto()
    HTTPS = auto()
    SOCKS5 = auto()


class ProxyStatus(Enum):
    pass


class ProxyInfo(NamedTuple):
    ip: str
    port: int
    status: ProxyStatus
    type: ProxyType


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
