#! python3
import keyboard
import pyautogui

print('Press Ctrl-C to quit.')

isDown = False

while True:
    keyboard.wait('P')
    x, y = pyautogui.position()
    if isDown:
        pyautogui.mouseUp(x, y, 'left')
    else:
        pyautogui.mouseDown(x, y, 'left')
    isDown = True
