import pywinauto
import os
import pyautogui

app = pywinauto.Application(backend='uia')

APP_DIR = f'{os.path.split(os.getenv("APPDATA"))[0]}\\Local\\VtopeBot'

path = os.path.join(APP_DIR, 'vtopebot.exe')

app = app.connect(path=path)

pane = app.Pane


pane.child_window(control_type='List', ctrl_index=0).draw_outline()
r = pane.child_window(control_type='List', ctrl_index=0).rectangle()

pywinauto.mouse.click(coords=(int(r.left + ((r.right - r.left) / 2)), int(r.top - (r.top - r.bottom) / 2)))

while True:
    #r = pane.child_window(control_type='List', ctrl_index=0).rectangle()

    #pywinauto.mouse.click(coords=(int(r.left + ((r.right - r.left) / 2)), int(r.top - (r.top - r.bottom) / 2)))
    pyautogui.scroll(-5)
