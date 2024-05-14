import sys
import random
from enum import Enum

def game() :
    class RPS(Enum) :
        ROCK = 1
        PAPER = 2
        SCISSORS = 3

    playerchoice = input("Enter... \n1 for Rock, \n2 for Paper, or \n3 for Scissors:\n\n")
    if playerchoice.isdigit() :
        player = int(playerchoice)
    else :
        print('Requires numeric inputs')

    if player < 1 or player > 3 :
      sys.exit('You must enter 1, 2 or 3')

    computerchoice = random.choice('123')
    computer = int(computerchoice)

    print(f'\nYou chose: {str(RPS(player)).replace('RPS.', '')}.')
    print(f'Python chose: {str(RPS(computer)).replace('RPS.', '')}. \n')

    if player == 1 and computer == 3:
        print("🎉 You win!")
    elif player == 2 and computer == 1:
        print("🎉 You win!")
    elif player == 3 and computer == 2:
        print("🎉 You win!")
    elif player == computer:
        print("😲 Tie game!")
    else:
        print("🐍 Python wins!")
    
    start_game()

def start_game() :
    print('')
    print('Start a game of Rock Paper Scissors with 🐍Python? ')
    answer = input('Pres `y` to start: \n').lower()
    if answer == 'y' :
        game()
    else :
        print('\n🎉 Thank you for visiting Rock Paper Scissors with 🐍Python!\n')

start_game()