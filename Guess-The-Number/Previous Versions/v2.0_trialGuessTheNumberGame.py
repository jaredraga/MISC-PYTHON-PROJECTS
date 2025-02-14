import random

guessesTaken = 0

number = random.randint(1, 20)

playAgain = 'yes'
while playAgain == 'yes' or playAgain == 'y':

    print('Hello! What is your name?')
    myName = input()
			print('Well, ' + myName + ', I am thinking of a number between 1 and 20.

    while guessesTaken < 6:
    
        guessesLeft = 6 - guessesTaken

        guessesLeft = str(guessesLeft)

        print('Take a guess.')
        guess = input()
        guess = int(guess)

        if guess < number:
            print('Your guess is too low.')

        if guess > number:
            print('Your guess is too high.)

        if guess == number:
            break


    if guess == number:
        guessesTaken = str(guessesTaken)

        print('Good Job, ' + myName + '')
        print('You guessed the number in ' + guessesTaken + ' guesses.')


    if guess != number:
        number = str(number)

        print('Nope. The number I was thinking of was ' + number + ' ')

    print('Do yoy want to play again? (yes/no) ')
    playAgain = input()    