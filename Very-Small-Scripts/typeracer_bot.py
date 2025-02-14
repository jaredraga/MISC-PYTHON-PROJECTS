import pyautogui
import random
import time

pyautogui.FAILSAFE = True

the_text = '''.'''
print('Typing in...')
t = 3
for i in range(t):
	time.sleep(1)
	print(t)
	t -= 1


pyautogui.typewrite(the_text)#, interval=random.uniform(0.05,0.07))
