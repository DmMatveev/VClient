from enum import Enum, auto
from typing import List

import commands
from common.proxy import ProxyInfo


class ProxyGetStatus(Enum):
    FOUND = auto()
    NOT_FOUND = auto()


class Get(commands.Command):
    RPC = False

    def __init__(self, ip):
        self.ip = ip

        super().__init__()

    def execute(self):
        proxies_info: List[ProxyInfo] = commands.proxy.List().data
        for proxy_info in proxies_info:
            if self.ip in proxy_info.ip:
                return ProxyGetStatus.FOUND

        return ProxyGetStatus.NOT_FOUND
