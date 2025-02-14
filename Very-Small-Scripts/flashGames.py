import pyautogui
import time

pyautogui.FAILSAFE = True

try:
	while True:
		pyautogui.click()
		time.sleep(.1)
		#pyautogui.press('')
except KeyboardInterrupt:
	print('Finished.')