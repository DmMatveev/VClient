from enum import Enum, auto

import commands


class ProxyGetStatus(Enum):
    FOUND = auto()
    NOT_FOUND = auto()


class Get(commands.Command):
    RPC = False

    def __init__(self, ip):
        self.ip = ip

        super().__init__()

    def execute(self):
        proxies_info = commands.proxy.List.get_all_proxies_info()
        for account_info in proxies_info:
            if self.login in account_info:
                return AccountGetStatus.FOUND, None

        return AccountGetStatus.NOT_FOUND, None
