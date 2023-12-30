#buisness is multi game where score is added to players when dice is rolled, each player gets unlimited tries until he gets 1.
#if the person gets 1 he's score become zero or else it will be added to his score and first person to complete score 69 wins the game
import random


def dice():
    dice= random.randint(1,6)
    return dice
while(True):
    print("------WELCOME TO THE GAME------ ")
    players=input("enter the no of players : ")
    if players.isdigit():
        players =int (players)
    if 2<=players<=5 :
        break
    else:
        print("invalid no of players  and  must be within 2-5")
    
    
winscore=69
playerscore=[0 for _ in range(players)]

while max(playerscore) < winscore:
    
    for player_id in range(players):

        print("\n player number ",player_id+1,"your turn has started !\n")
        curscore = 0
        while True:
            should_roll =input("would like to roll (y/n): ")
            if should_roll.lower() != "y":
               win=input("Do you want to declare other player if yes ?? ")
               if win.lower()=='y':
                    winner_id = int(input("Enter the player ID to declare as the winner: "))
                    if winner_id == player_id + 1:
                            print(f"Player {winner_id} is the winner!")
                            # Declare the winner when the loop exits
                            winner_id = playerscore.index(max(playerscore)) + 1
                            print(f"\nPlayer {winner_id} is the overall winner with a score of {playerscore[winner_id - 1]}!")  
                            exit()

            value=dice()
            if value == 1:
                print("You rolled a 1!,your Turn is over and lost everything🥲")
                print ("better luck next time \n")
                curscore=0
                break
            else:
                print("you got: ",value)
                print(f"{curscore}+{value}")
                curscore +=value 
                print(f"Your score is :{curscore}")

        playerscore[player_id]+=curscore
        print("your total score is :",playerscore[player_id])


   
    