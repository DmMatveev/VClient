try:
    import pywinauto
    import os
    import locale
except Exception as e:
    print(type(e))
    print(e)
    input()

def getpreferredencoding(do_setlocale = True):
    return "utf-8"

locale.getpreferredencoding = getpreferredencoding

def init():
    try:
        app = pywinauto.Application(backend='uia')

        APP_DIR = f'{os.path.split(os.getenv("APPDATA"))[0]}\\Local\\VtopeBot'

        path = os.path.join(APP_DIR, 'vtopebot.exe')

        app = app.connect(path=path)

        pane = app.Pane

        #pane.print_control_identifiers(depth=1000, filename='info.txt')

    except Exception as e:
        print(e)
        input()

    input()

if __name__ == '__main__':
    init()
