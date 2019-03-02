from vclient import commands


#TODO ListBox0 пропал

class List(commands.Command):
    list = 'ListBox0'
    status = ['badauth', 'validating', 'manual']

    def _check_status(self, info):
        for status in self.status:
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

    def get_accounts(self):
        # TODO проверить когда нет аккаунтов
        #TODO проверить что пусто
        return self.pane[self.list].children()

    def execute(self):
        items = []

        for account in self.get_accounts():
            info = account.element_info.name

            if info.endswith('widget'):
                info = info[1:info.rindex('1')]
                status = self._check_status(info)

                login = info.replace(status, '')
                login = self._clean_login(login)

                items.append({
                    'login': login,
                    'status': status
                })

        return items

