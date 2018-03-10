import random

rps = ['rock', 'paper', 'scissors']
while True:
    while True:
        user_choice = input('rock, paper, or scissors? ').lower()
        if user_choice == 'rock' or user_choice == 'paper' or user_choice == 'scissors':
            break
        if user_choice != 'rock' or user_choice != 'paper' or user_choice != 'scissors':
            print('please enter a valid choice, not ' + user_choice)

    print('user choice: ' + user_choice)

    comp_choice = random.choice(rps)
    print('computer choice: ' + comp_choice)

    if user_choice == comp_choice:
        print('tie!')
    elif user_choice == 'rock' and comp_choice == 'paper':
        print('computer wins!')
    elif user_choice == 'rock' and comp_choice == 'scissors':
        print('user wins!')
    elif user_choice == 'paper' and comp_choice == 'rock':
        print('user wins!')
    elif user_choice == 'paper' and comp_choice == 'scissors':
        print('computer wins!')
    elif user_choice == 'scissors' and comp_choice == 'rock':
        print('computer wins!')
    elif user_choice == 'scissors' and comp_choice == 'paper':
        print('user wins!')

    while True:
        play_again = input("Do you want to play again").lower()
        if play_again == 'yes' or play_again == 'no':
            break
    if play_again == 'no':
        break
