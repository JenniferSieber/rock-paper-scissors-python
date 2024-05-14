import sys
import random
from enum import Enum

print('Rock Paper Scisssors against Pyhon 🐍')
def play_rps():

    class RPS(Enum):
        ROCK = 1
        PAPER = 2
        SCISSORS = 3

    p_choice = input( "\nEnter... \n1 for Rock,\n2 for Paper, or \n3 for Scissors:\n\n")

    if p_choice not in ['1', '2', '3'] :
        print('You must enter a 1, 2, or 3.')
        return play_rps()
    
    player = int(p_choice)
    c_choice = random.choice('123')
    computer = int(c_choice)

    print(f'You chose: {str(RPS(player)).replace('RPS.', '').title()}.')
    print(f'Python chose: {str(RPS(computer)).replace('RPS.', '').title()}.')

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

    print("\nPlay again?")

    while True :
        playagain = input('\nY for Yes or \nQ to Quit\n').lower()
        if playagain not in ['y', 'q'] :
            continue
       
        if playagain == 'y' :
            return play_rps()
        
        else :
            print("\n🎉🎉🎉🎉")
            print("Thank you for playing!\n")
            sys.exit("Bye! 👋")

play_rps()