#! python3
import pyautogui

print('Press Ctrl-C to quit.')

# Get and print the mouse coordinates.
x, y = pyautogui.position()
pyautogui.click(x, y)
