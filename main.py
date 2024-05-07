"""
Rock Paper Scissors:
Provided announcement of game and permission to start running the game.
Play standard version or Rock Paper Scissors 
For each round: take user answer and provided a randomly generated answer from the Computer.
Compare the answers to win conditions and annouce winner
and running score for each party at end of round.
The user may play as many rounds as they want.

"""
import random 
print(' ✂️  Welcome to Rock Paper Scissors! ✂️ '.upper())
print(' 🤖 Play against a Computer to see who can get the best score! 🤖')

def start_game() :
    print()
    play = input('Do you want to play a game --yes or no ?  ').lower()
    if play == 'yes' :
        print("Let's Play! 🥳")
        game_play()

    elif play != 'yes' :
      print('  😔 Maybe another time.')
      quit()

def game_play() :
    user_wins = 0
    computer_wins = 0
    options = ['rock', 'paper', 'scissors']
    win_conditions = {'rock': 'scissors', 'paper': 'rock', 'scissors': 'paper'}

    while True :
        print()
        user_choice = input('Rock-Paper-Scissors or Q to quit: ').lower()
        if user_choice == 'q' :
            break
        if user_choice not in options :
            continue

        if user_choice in options :
            random_i = random.randint(0,2)
            computer_choice = options[random_i]
            if computer_choice == win_conditions.get(user_choice) :
                user_wins += 1
                print(' 🥳 You won!', 'Computer chose: ', computer_choice)
                print('Wins: You:', user_wins, ' vs. Computer:', computer_wins)
               
            elif user_choice == win_conditions.get(computer_choice) :  
                computer_wins += 1          
                print(' 🤖 Computer won with: ', computer_choice)
                print('Your current wins:', user_wins, 'Computer wins:', computer_wins)
                
                
            elif user_choice == computer_choice :
                print('It is a Tie! Computer chose: ', computer_choice)
                print('Wins: You', user_wins, ' vs. Computer:', computer_wins)
                
          
    print(' ✂️  Quit Rock Paper Scissors, Good-bye. ✂️ ') 
    start_game()      
       
start_game()   
