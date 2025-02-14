# Author: Jared I. Raga ©2018
# Email: jir@gmail.com
# Beginning  Date: 7/25/18 8:30PM
# Completion Date: 7/25/18 8:45PM
# Program Name: Mouse Live -- Shows the mouse's current x, y position
# Program Ver.: 1.0.0

import pyautogui
import sys

pyautogui.FAILSAFE = True

print('Press Ctrl-C to quit.')
try:
	while True:
		x, y = pyautogui.position()
		# The rjust() string method will right-justify them so
		# that they take up the same amount of space, whether the coordinate has
		# one, two, three, or four digits.
		sys.stdout.write("\r%s" % 'X:' + str(x).rjust(4) + ' Y:' + str(y).rjust(4)) 
		sys.stdout.flush()
except KeyboardInterrupt:
	print('\n Done.')
