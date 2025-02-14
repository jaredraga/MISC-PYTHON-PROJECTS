import pyautogui, time

while True:
	
	time.sleep(4)
	pyautogui.click(265, 15)
	time.sleep(.1)
	pyautogui.moveTo(327, 68, 1, pyautogui.easeOutQuad)
	pyautogui.click(327, 68)
	time.sleep(3)
	pyautogui.typewrite('python3 botOpeningItself.py')
	pyautogui.press('enter')
	time.sleep(1)
	pyautogui.hotkey('alt', 'esc')
	time.sleep(1)
	pyautogui.hotkey('alt', 'f4')

