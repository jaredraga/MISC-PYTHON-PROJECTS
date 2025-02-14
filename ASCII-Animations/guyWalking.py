import time

MAN = ['''

 π
 O/
/|
 LL''',''' 
 
  π
  O/
 /|L
  L ''','''

   π
   O
  /|\\
   LL''','''
   
    π
   \O
    |L
     L''','''  
  
     π
     O
    /|\\
     LL''','''
             
      π
      O/
     /|L
      L ''','''

        π
        O
       /|\\
        LL''','''
 
         π
        \O
         |L
         L''','''
  
          π
          O
         /|\\
          LL''']

cycle = 0
while True:
    print(" "*10000)    
    print(MAN[cycle])
    time.sleep(0.1)   
    cycle = cycle + 1    
    if cycle == 9:
        cycle = 0                          