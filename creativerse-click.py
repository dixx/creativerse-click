#! python3
import pyautogui, time

print('Press Ctrl-C to quit.')
time.sleep(27)
for i in range(3):
    print '\a'
    time.sleep(1)

x, y = pyautogui.position()
mouseDown(x, y, 'left')
