# Author: Jared I. Raga ©2018
# Email: jir@gmail.com
# Beginning  Date: 8/27/18 10:50PM
# Completion Date: 8/27/18 11:41PM
# Program Name: White Bag Probability Tester
# Program Ver.: 1.0.0

import random

# Flowchart

# Create a drop table containing the possible items you could get
PROBABILITY = 1000
num_runs = 0
unlucky_runs = 0
unluckiest_run = 0
luckiest_run = PROBABILITY * 99999
num_tests = 0
while True:
	num_runs += 1
	white_bag = random.randint(1, PROBABILITY)
	acquired_loot = random.randint(1, PROBABILITY)

	if acquired_loot == white_bag:
		num_tests += 1

		print('White Bag acquired within %s runs on a 1/%s probability.' % (num_runs, PROBABILITY))

		if num_runs > PROBABILITY:
			unlucky_runs += 1
		print('Runs that exceeded probability:%s/%s' % (unlucky_runs, num_tests))

		if num_runs < luckiest_run:
			luckiest_run = num_runs
		print('Luckiest: %s runs before White Bag.' % luckiest_run)

		if num_runs > unluckiest_run:
			unluckiest_run = num_runs
		print('Unluckiest: %s runs before White Bag.' % unluckiest_run)
			
		num_runs = 0

		print()
		
		if unluckiest_run >= 10000 or num_tests >= 25000:
			unlucky_runs = 0
			unluckiest_run = 0
			luckiest_run = PROBABILITY * 99999
			num_tests = 0
			input()

