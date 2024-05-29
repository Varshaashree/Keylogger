from pynput.mouse import Controller
from pynput.keyboard import Controller
#(left to right,top to bottom->from top left)
def controlMouse():
    mouse=Controller()
    mouse.position=(800,100)
#controlMouse()
def controlKey():
    keyboard=Controller()
    keyboard.type("heloo world")
controlKey()



