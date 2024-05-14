import sys 
import random 
from enum import Enum 

class RPS(Enum) :
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

playagain = True

while playagain :
    p_choice = input( "\nEnter... \n1 for Rock,\n2 for Paper, or \n3 for Scissors:\n\n")

    p = int(p_choice)
    if p < 1 or p > 3 :
        sys.exit('You must enter 1, 2, or 3')
    
    c_choice = random.choice('123')
    c = int(c_choice)

    print(f"You chose: {str(RPS(p)).replace('RPS.', '').title()}.")
    print(f"Python chose: {str(RPS(p)).replace('RPS.', '').title()}.")

    if p == 1 and c == 3:
        print("🎉 You win!")
    elif p == 2 and c == 1:
        print("🎉 You win!")
    elif p == 3 and c == 2:
        print("🎉 You win!")
    elif p == c:
        print("😲 Tie game!")
    else:
        print("🐍 Python wins!")

    playagain = input("\nPlay again? \nY for Yes or \nQ to Quit \n\n")

    if playagain.lower() == "y":
        continue
    else:
        print("\n🎉🎉🎉🎉")
        print("Thank you for playing!\n")
        playagain = False

sys.exit("Bye! 👋")
