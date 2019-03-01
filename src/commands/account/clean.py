from src import commands


class Clean(commands.Command):
    def execute(self):
        accounts = commands.List().execute()

        for account in accounts:
            commands.Delete(account['login']).execute()

