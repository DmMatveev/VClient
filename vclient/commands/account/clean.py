import commands


class Clean(commands.Command):
    def execute(self):
        accounts = commands.List().result

        for account in accounts:
            commands.Delete(account['login'])

