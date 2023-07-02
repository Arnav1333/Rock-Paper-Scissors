import random
c = ['Rock','Paper','Scissors']
while True:
    player = input("Enter Rock/Paper/Scissors: ")
    
    
    computer = random.choice(c)
    print(computer)
    
    
    if player == computer:
        print("Its a tie!")
    elif player == 'Rock':
        if computer == 'Paper':
            print("You lost!")
        else:
            print("You Won!")
    elif player == 'Paper':
        if computer == 'Scissors':
            print("You lost!")
        else:
            print("You Won!")
    elif player == 'Scissors':
        if computer == 'Rock':
            print("You lost!")
        else:
            print("You Won!")

    play_again = input('Play again? (y/n)')
    if (play_again.lower() == 'n'):
        break

