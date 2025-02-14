import time
import sys

timeout = int(input('Timeout:'))

start = time.time()
while True:

	time_elapsed = int(time.time() - start)

	sys.stdout.write("\r%s" % str(time_elapsed) + ' seconds(s) elapsed')
	sys.stdout.flush()

	if time.time() - start >= timeout:
		print('\n' + str(timeout) +' seconds is up!')
		break
	