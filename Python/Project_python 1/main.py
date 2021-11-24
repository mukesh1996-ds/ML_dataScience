"""
In this we are going to develop a game.
SNAKE WATER GUN GAME
"""
import random

def game_win(computer_turn,your_turn):
    if computer_turn == your_turn:
        return None
    elif computer_turn == 's':
        if your_turn == 'w':
            return False
        elif your_turn == 'g':
            return True
    elif computer_turn == 'w':
        if your_turn == 'g':
            return False
        elif your_turn == 's':
            return True
    elif computer_turn == 'g':
        if your_turn == 's':
            return False
        elif your_turn == 'w':
            return True

randno = random.randint(1,3)
print(randno)
computer_turn = input('Computer turn : Snake(s) Water(w) or gun(g)?')
if randno == 1:
    computer_turn = 's'
elif randno == 2:
    computer_turn = 'w'
else:
    computer_turn = 'g'

your_turn = input("Player's turn : Snake(s) Water(w) or gun(g)?")
a = game_win(computer_turn, your_turn)

print(f'computer choose {computer_turn}')
print(f'you choose {your_turn}')


if a == None:
    print('The game is TIE!')
elif a:
    print('You WIN!')
else:
    print('you LOOSE')
    

