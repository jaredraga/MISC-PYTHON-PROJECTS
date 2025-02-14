import random
import pyautogui
import time

pyautogui.PAUSE = 0.03
pyautogui.FAILSAFE = True

# countdown
t = 4
for i in range(t):
	print(t)
	time.sleep(1)
	t -= 1
# main code
while True:
	# choose random 1,9 and type that to keyboard
	pyautogui.typewrite(random.randint(1, 9))
	pyautogui.press('enter')

