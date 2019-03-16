import pywinauto
import os
import pyautogui

app = pywinauto.Application(backend='uia')

APP_DIR = f'{os.path.split(os.getenv("APPDATA"))[0]}\\Local\\VtopeBot'

path = os.path.join(APP_DIR, 'vtopebot.exe')

app = app.connect(path=path)

pane = app.Pane

pane.child_window(title="backgroundModalWidget", control_type="Custom").parent().children()[1].children()

pane.print_control_identifiers(depth=1000)

pane.child_window(title="backgroundModalWidget", control_type="Custom").click()
