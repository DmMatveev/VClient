import commands
from commands import utils
from common.proxy import ProxyStatus, ProxyInfo, ProxyType


class List(commands.Command):
    RPC = False

    def execute(self):
        list_box = self.pane.child_window(control_type='List', ctrl_index=1)
        return None, list(map(self.get_proxy_info, utils.get_all_items_info_string(list_box)))

    def get_proxy_info(self, proxy_info_string) -> ProxyInfo:
        proxy_info_string = utils.clean_info_string(proxy_info_string)

        status = self.get_proxy_status(proxy_info_string)
        proxy_info_string = self.clean_status(proxy_info_string, status)

        type_ = self.get_proxy_type(proxy_info_string)

        ip, port = proxy_info_string.split(type_.name.lower())

        return ProxyInfo(ip, int(port), status, type_)

    def get_proxy_status(self, proxy_info_string: str) -> ProxyStatus:
        for status in ProxyStatus:
            if status.name in proxy_info_string:
                return status

        raise AttributeError('Статус прокси не найден')

    def clean_status(self, proxy_info_string: str, status: ProxyStatus):
        return proxy_info_string.replace(status.name, '')[1:]

    def get_proxy_type(self, proxy_info_string: str) -> ProxyType:
        for type_ in ProxyType:
            if type_.name.lower() in proxy_info_string:
                return type_
