#! python3
import pyautogui, time

print('Press Ctrl-C to quit.')
time.sleep(27)
for i in range(3):
    print '\a'
    time.sleep(1)

# Get and print the mouse coordinates.
x, y = pyautogui.position()
pyautogui.click(x, y)
