import pyautogui
import time
import random

pyautogui.FAILSAFE = True

#click browser
pyautogui.moveTo(1311, 73, duration=3)
pyautogui.doubleClick(1311, 73)

time.sleep(5)

#click search field
pyautogui.click(418, 107)

#delete link if there's any
pyautogui.hotkey('ctrl', 'a')
pyautogui.press('backspace')

#open clicker counter game
pyautogui.typewrite('www.scratch.mit.edu/projects/545855/')
pyautogui.press('enter')

time.sleep(3)

pyautogui.confirm('Activate the clicker bot?')

#  clicks
pyautogui.click(x=325, y=545, clicks=10000, interval=0, button='left')
