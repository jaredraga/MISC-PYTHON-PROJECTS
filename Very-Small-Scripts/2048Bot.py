import pyautogui
import random
import time

pyautogui.FAILSAFE = True

while True:
	r = random.randint(1,4)

	if r == 1:
		pyautogui.press('up')

	elif r == 2:
		pyautogui.press('left')

	elif r == 3:
		pyautogui.press('down')

	elif r == 4:
		pyautogui.press('right')

	time.sleep(0.05)
	pyautogui.click(x=645, y=510)
