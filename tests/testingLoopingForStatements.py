import time
        
spam = '--We-reached-69--'
spam2= 'test'
dot = '•' * len(spam)

cycle = 0
TEST = ['''

L
O
L

''']
while True:

    for i in range(len(spam)) and t in range(len(spam2)):
        print(' ' * 5000)
        print(TEST[0])
        print(spam[:i] + dot[i] + spam[i+1:])
        print(spam2[:t] + dot[t] + spam2[t+1:])
                
        time.sleep(0.1)