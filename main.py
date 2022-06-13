import random

# Welcome greeting and declaration of rules
welcome = 'Rock Paper and Scissors game!!!'
rule = ''' 
--- This is the rule of the game ---
If the two players choose the same character it's a tie, and the game repeats
Rock beats Scissors
Paper beats Rock
Scissors beats Paper
 '''
print(welcome, rule)

# Game option in a list
game_option = ['Rock', 'Paper', 'Scissors']

# User and computer input
player_1 = 0 #This is the user
player_2 = 0 #This is the computer

# The loop for the game
while True:
    # Ask for player input
    player_input = input('pick from the available options "Rock" "Paper" "Scissors": ')
    player_1 =  player_input

    # Setting the computer to pick from the list at random
    player_2 = random.choice(game_option)
    
    # Display both what the user and computer have picked
    print(f'Player ({player_1}) : CPU ({player_2})')

    # The conditions to be met when the user picks rock
    if player_1 == 'Rock' and player_2 == 'Paper':
        print('Paper beats Rock! You Lose ')
        break
    elif player_1 == 'Rock' and player_2 == 'Scissors':
        print('Rock beats Scissors! You Win ')
        break
    elif player_1 == 'Rock' and player_2 == 'Rock':
        print('Rock and Rock! This is a Tie, Play again!')
        continue

    # The conditions to be met when the user picks rock
    elif player_1 == 'Paper' and player_2 == 'Rock':
        print('Paper beats Rock! You Win ')
        break
    elif player_1 == 'Paper' and player_2 == 'Scissors':
        print('Scissors beats Paper! You Lose ')
        break
    elif player_1 == 'Paper' and player_2 == 'Paper':
        print('Paper and Paper! This is a Tie, Play again!')
        continue

    # The conditions to be met when the user picks rock
    elif player_input == 'Scissors' and player_2 == 'Rock':
        print('Rock beats Scissors! You Lose ')
        break
    elif player_input == 'Scissors' and player_2 == 'Paper':
        print('Scissors beats Paper! You Win ')
        break
    elif player_input == 'Scissors' and player_2 == 'Scissors':
        print('Scissors and Scissors! This is a Tie, Play again!')
        continue

    # If the user input isn't a part of the options listed
    else:
        print('Error!')