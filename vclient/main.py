# self.app.print_control_identifiers(depth=1000)

import pywinauto
app = pywinauto.Application(backend='uia')
app.connect(path='C:\\Users\\Dmitry\\AppData\\Local\\VtopeBot\\vtopebot.exe')


def init():
    while True:
        pass
        #считать комманду
        #выполнить команду
        #вернуть результат



if __name__ == '__main__':
    init()