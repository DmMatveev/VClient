from vclient import commands

'''
Окна:
Auth,
Ready,
ReadyNoInternet
'''


class Status(commands.Command):
    def execute(self):
        if commands.application.Auth.is_auth():
            return True


