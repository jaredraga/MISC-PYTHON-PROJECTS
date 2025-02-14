import time

sequence = ['cats', 'pasta', 'programming', 'spam'] 
cycle = 0 
while (cycle < len(sequence)): 
        thing = sequence[cycle] 
        print('I really like ' + thing)
        time.sleep(0.3)
        cycle = cycle + 1 