from random import choice
from string import ascii_lowercase as low
def hangman():
    choosen = list(choice(['python', 'java', 'kotlin', 'javascript']))
    hidden = list('-' * len(choosen))
    prev = set()
    print('H A N G M A N')
    j = 8
    while j != 0:
        if choosen == hidden:
            print(''.join(hidden))
            break
        print()
        print(''.join(hidden))
        guess = input('Input a letter: ')
        if len(guess) != 1:
            print('You should input a single letter')
            continue
        elif guess not in low:
            print('It is not an ASCII lowercase letter')
            continue
        elif guess in prev:
            print('You already typed this letter')
            continue
        elif guess in choosen:
            for i in range(len(choosen)):
                if choosen[i] == guess:
                    hidden[i] = guess
        elif guess not in choosen:
            j -= 1
            print('No such letter in the word')
        prev.add(guess)
    if choosen == hidden:
        print("You guessed the word!\nYou survived!")
    else:
        print('You are hanged!')

choose = ''
while choose != 'play' or choose != 'exit':
    choose = input('Type "play" to play the game, "exit" to quit: > ')
    if choose == 'play':
        print()
        hangman()
    if choose == 'exit':
        break
