# Author: Jared I. Raga ©2018
# Email: jir@gmail.com
# Beginning  Date: 7/?/18
# Completion Date: 7/?/18
# Program Name: ROTMG_Trading_Bot
# Program Ver.: 1.0.0

import pyautogui
import time
import random
import sys
import os

pyautogui.FAILSAFE = True

trade_offers = [
    "Buying 3L for 5Defs",
    "Selling 2Mana for 6L",
    "Trading 8SPD for 3DEF",
    "Buying 5Wis for 2Life",
    "Selling 10ATT for 4Mana",
    "Trading 1Life for 3Dex"
]

def countdown(t):
    for i in range(t, 0, -1):
        time.sleep(1)
        print(i)

def get_random_trade():
    return random.choice(trade_offers)

print('Posting trade offers in:')
countdown(3)

while True:
    pyautogui.press('enter')
    pyautogui.typewrite(get_random_trade())
    pyautogui.press('enter')
    time.sleep(3)
