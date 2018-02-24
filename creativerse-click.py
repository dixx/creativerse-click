#! python3
import keyboard
import pyautogui


def toggleMouse(state):
    x, y = pyautogui.position()
    if state:
        pyautogui.mouseUp(x, y, 'left')
    else:
        pyautogui.mouseDown(x, y, 'left')


print('Press SHIFT+P to toggle mouse up/down, SHIFT+ESC to quit.')

isDown = False
running = True

while running:
    key = keyboard.read_hotkey()
    if key == 'shift+esc':
        running = False
    if key == 'shift+p':
        toggleMouse(isDown)
        isDown = not isDown
