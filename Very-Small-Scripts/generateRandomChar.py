# The same with my shortStr.py and takes up less lines but uglier.

import random, string 

while True:
    x = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase) for _ in range(8)) 

    print(x)
    input()