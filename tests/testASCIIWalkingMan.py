import time

MAN = ['''
 π
 O
/|\\
/ \\''','''

 π
 O
/|\\
/ L''','''

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
   \\O
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
      \\O
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
          \\O
           |L
           L''','''











  
            π
            O
           /|\\
            LL''']
            
SPACES = ['''

























































''']

cycle = 0

while True:
    print(SPACES[0])
    print(MAN[cycle])
    time.sleep(0.6)
    
    cycle = cycle + 1
    if cycle == 11:
        cycle = 0