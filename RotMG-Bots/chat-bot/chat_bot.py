# Author: Jared I. Raga ©2018
# Email: jir@gmail.com
# Beginning  Date: 7/?/18
# Completion Date: 7/?/18
# Program Name: ROTMG_Chat_Bot
# Program Ver.: 1.0.0

import pyautogui
import time
import random
import sys
import os

pyautogui.FAILSAFE = True

def countdown(t):
	for i in range(t):
		time.sleep(1)
		print(t)
		t -= 1

def summon_dick():
	dick_length = random.randint(1,7)
	dick = '3' + '='*dick_length + 'D'

	return dick
model = '''
                                      3==D
                                   3==D~
3==D~~~~~~~~~~~~~'''
def rocket_dick(first_phase, second_phase, cum_length):
	if first_phase != 38:	
		first_phase += 1
		return first_phase, second_phase, cum_length, ' ' * first_phase + '3==D'
	
	if first_phase >= 38 and cum_length < 13:
		second_phase += 3
		cum_length += 1
		return first_phase, second_phase, cum_length, ' ' * (38 - second_phase) + '3==D' + '~' * cum_length

def cum_dick():
	first_phase = 0
	second_phase = 0
	cum_length = 0
	while True:

		first_phase, second_phase, cum_length, text = rocket_dick(first_phase, second_phase, cum_length)

		pyautogui.press('enter')	
		pyautogui.typewrite(text)
		pyautogui.press('enter')
		time.sleep(0.00001)
		
		if cum_length >= 13:
			first_phase = 0
			second_phase = 0
			cum_length = 0
		
print('Typing in in:')
countdown(3)

while True:
	pyautogui.press('enter')
	pyautogui.typewrite(summon_dick())
	pyautogui.press('enter')
	time.sleep(1)