import random
weapons = ['rock', 'paper', 'scissor']
player_1 = input("Enter your choice : ")
print(f"Your choice is {player_1}")
player_comp = weapons [random.randint(0 , 2)]
print(f"Computer choses {player_comp}")

if player_1 == 'rock':
    if player_comp == 'paper':
        print("Computer wins")
    elif player_comp == 'scissor':
        print("You win !")
    elif player_comp == 'rock':
        print("It's a tie")   

if player_1 == 'paper':
    if player_comp == 'scissor':
        print("Computer wins")
    elif player_comp == 'rock':
        print("You win !")
    elif player_comp == 'paper':
        print("It's a tie")   

if player_1 == 'scissor':
    if player_comp == 'rock':
        print("Computer wins")
    elif player_comp == 'rock':
        print("You win !")
    elif player_comp == 'scissor':
        print("It's a tie")   
        

    

