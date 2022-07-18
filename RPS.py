import random

print("Welcome to Rock, Paper and Scissor")
goal =3

#starting player points
start_p=0

#starting computer points
start_c=0

#list of all the moves
moves=["Rock","Paper","Scissor"]


#function to identify the winner
def descision(c,p):
    global start_p,start_c
    if c=="Rock" and p=="Paper":
        start_p=start_p+1
        print("Player: " + str(start_p))
        print("Computer: " + str(start_c))
    elif p=="Rock" and c=="Paper":
        start_c=start_c+1
        print("Player: " + str(start_p))
        print("Computer: " + str(start_c))
    elif p=="Paper" and c=="Scissor":
        start_c=start_c+1
        print("Player: " + str(start_p))
        print("Computer: " + str(start_c))
    elif p=="Scissor" and c=="Rock":
        start_c=start_c+1
        print("Player: " + str(start_p))
        print("Computer: " + str(start_c))
    elif p=="Rock" and c=="Scissor":
        start_p=start_p+1
        print("Player: " + str(start_p))
        print("Computer: " + str(start_c))
    elif p=="Scissor" and c=="Paper":
        start_p=start_p+1
        print("Player: " + str(start_p))
        print("Computer: " + str(start_c))
    
    if(start_c<3 and start_p<3):
        print("")
        game()
    else:
        print("")
        if(start_c==3):
            print("You Lost:(")
        else:
            print("You Won:)")

#user interaction
def game():
    c_move=random.choice(moves)
    print("Round: " +str(start_c+start_p+1))
   
    p_choice = int(input("What is your move Rock[0] , Paper[1], Scissors[2]: "))
    p_move=moves[p_choice]
  
    print("Computer player: " + c_move)
    print("Player Moved: " + p_move)

    descision(c_move, p_move)



game()