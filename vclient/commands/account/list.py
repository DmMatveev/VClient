import commands


class List(commands.Command):
    ACCOUNT_STATUS = ['badauth', 'validating', 'manual']

    def _check_status(self, info):
        for status in self.ACCOUNT_STATUS:
            if status in info:
                return status

        raise Exception()

    def _clean_login(self, login):
        # Хак, появляются рандомные числа в наименование
        # Закономерность, что эти числа заканичвается одинаково и они одинакового размера
        if '_' in login:
            number_size = login.rindex('_') - login.index('_') - 1
            login = login[number_size * 2 + 2:]

        return login

    @classmethod
    @commands.utils.wait_before(1)
    def get_accounts(cls):
        items = cls.pane.child_window(control_type='List', ctrl_index=0).children()
        result = []

        for item in items:
            info = item.element_info.name
            if info.endswith('widget'):
                result.append(item)

        return result

    def execute(self):
        items = []

        for account in self.get_accounts():
            info = account.element_info.name

            info = info[1:info.rindex('1')]

            status = self._check_status(info)
            login = info.replace(status, '')
            login = self._clean_login(login)
            items.append({
                'login': login,
                'status': status
            })

        self.data = items

