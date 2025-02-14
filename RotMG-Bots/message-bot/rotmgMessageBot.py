#l3072980@nwytg.com
#burger1234


#Continue:
# Daily quest retrieval

import pyautogui
import time
import random

pyautogui.FAILSAFE = True

def openAndLogin():
	#click browser
	pyautogui.doubleClick(1311, 73)

	#wait for browser to open
	time.sleep(10)

	#click search field
	pyautogui.click(418, 107)

	#delete link if there's any
	pyautogui.hotkey('ctrl', 'a')
	pyautogui.press('backspace')

	#open rotmg
	pyautogui.typewrite('www.realmofthemadgod.com')
	pyautogui.press('enter')

	#wait for rotmg to load
	time.sleep(30)


	#login with bot account
	#double-click login button to logout past account
	pyautogui.moveTo(1043, 175, duration=1)
	pyautogui.doubleClick(1043, 175)
	#click email field and type email
	pyautogui.moveTo(620, 405, duration=1)
	pyautogui.click(620,405)
	pyautogui.typewrite('zzzzzzz@nwytg.com')
	#click password field and type password
	pyautogui.moveTo(629,476, duration=1)
	pyautogui.click(629,476)
	pyautogui.typewrite('burger1234')
	#click sign in button
	pyautogui.moveTo(772, 560, duration=1)
	pyautogui.click(772,560)

	#wait for account to sign in
	time.sleep(7)
	#click servers
	pyautogui.moveTo(588, 713, duration=2)
	pyautogui.click(588, 713)
	time.sleep(2)
	#scroll down
	pyautogui.scroll(-10)
	#click asia east
	pyautogui.moveTo(457, 647, duration=2)
	pyautogui.click(457, 647)
	#click done - play - play 
	pyautogui.tripleClick(688, 710, interval=1)

def questRoom():

	# go to nexus
	time.sleep(1)
	pyautogui.press('r')
	print('The bot is in the nexus')
	#maneuvering to the quest room
	time.sleep(10)
	pyautogui.keyDown('w')
	pyautogui.keyDown('d')
	time.sleep(2)
	pyautogui.keyUp('d')
	time.sleep(4)
	pyautogui.keyUp('w')

	pyautogui.keyDown('a')
	time.sleep(2)
	pyautogui.keyUp('a')

	pyautogui.keyDown('d')
	time.sleep(.4)
	pyautogui.keyUp('d')

	pyautogui.keyDown('s')
	time.sleep(.2)
	pyautogui.keyUp('s')

	#click enter button of quest room
	time.sleep(1)
	pyautogui.moveTo(969, 739, duration=2)
	pyautogui.click(983, 733)

	#wait for quest room to load
	time.sleep(10)
	print('The bot is in the quest room.')

	pyautogui.keyDown('w')
	time.sleep(1.8)
	pyautogui.keyUp('w')

	pyautogui.keyDown('a')
	time.sleep(1)
	pyautogui.keyUp('a')

	#click daily rewards button
	pyautogui.moveTo(969, 739, duration=2)
	pyautogui.click(983, 733)
	
		
def getBotCommand():

	print('What is it that you want the bot to do?')
	print('''Options:

	Message           -Message someone

	Daily Quest       -Retrieve the daily quest''')

	botCommand = ''
	while True:		
		botCommand = input('Bot Command:')

		if not (botCommand == 'Message' or botCommand == 'Daily Quest'):
			print('Invalid Input')
		else:
			break

	return botCommand




#botCommand = getBotCommand()

openAndLogin()
print('The bot has succesfully logged in.')
	
#questRoom()
#print('The bot has succesfully retrieved the daily quest')
time.sleep(10)

pyautogui.press('r')
print('The bot is in the nexus')
ascii_symbols = list('!"#$%&\'()*+-:@[]^_\{\}~')
while True:

	r = random.randint(2, 15)

    #Small == === ==== ===== ====== Medium ======= ======== ========= ========== Large =========== ============ ============= ============== ===============
	if r <= 6:
		size = 'Small'
	elif r <=9:
		size = 'Medium'
	elif r <= 10:
		size ='Large'
	pyautogui.press('enter')
	pyautogui.typewrite('I love dicks!')
	pyautogui.press('enter')
	time.sleep(1)
	pyautogui.press('enter')
	pyautogui.typewrite('3' + '=' * r + '>', interval = .05)
	pyautogui.press('enter')

	pyautogui.press('enter')
	pyautogui.typewrite(size + ' dicks!')
	pyautogui.press('enter')
	
	pyautogui.press('a')	

	pyautogui.press('d')

	time.sleep(10)
	






