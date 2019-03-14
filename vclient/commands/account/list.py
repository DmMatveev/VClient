import commands


class List(commands.Command):
    ACCOUNT_STATUS = ['badauth', 'validating', 'manual']

    def _check_status(self, info):
        for status in self.ACCOUNT_STATUS:
            if status in info:
                return status

        raise Exception()

    def clean_login(self, login: str) -> str:
        """
        Хак, появляются рандомные числа в наименование
        Закономерность, что эти числа заканичвается одинаково и они одинакового размера
        """
        if '_' in login:
            number_size = login.rindex('_') - login.index('_') - 1
            login = login[number_size * 2 + 2:]

        return login

    @classmethod
    @commands.utils.wait_before(1)
    def get_accounts(cls):
        result = set()

        while True:
            items = cls.pane.child_window(control_type='List', ctrl_index=0).children()

            items = [item.element_info.name for item in items if item.element_info.name.endswith('widget')]
            result.union(items)




    def execute(self):
        items = []

        for account in self.get_accounts():
            info = account.element_info.name

            info = info[1:info.rindex('1')]

            status = self._check_status(info)
            login = info.replace(status, '')
            login = self.clean_login(login)
            items.append({
                'login': login,
                'status': status
            })

        self.data = items

