from art_and_data import day11challenge_art
import os
import random
def logo():
    logo=day11challenge_art.logo
    print(logo)

def value(loop):
    computer=[]
    player=[]
    computer_score=0
    player_score=0
    dicvalue={}
    for x in range(0,loop):
        computer_draw=random.randint(1,10)
        player_draw=random.randint(1,10)
        computer.append(computer_draw)
        player.append(player_draw)       
        computer_score+=computer[x]
        player_score+=player[x] 
    dicvalue["computer_draw"]=computer
    dicvalue["player_draw"]=player
    dicvalue["computer_score"]=computer_score
    dicvalue["player_score"]=player_score
    return dicvalue

def black_jack():
    loop=2
    loop2=True
    values=value(loop)
    computer=values['computer_draw']
    player=values['player_draw']
    computer_score=values['computer_score']
    player_score=values['player_score']
    

    while loop2:
        def message():            
            print(f"Your final hand: {player}, final score: {player_score}")
            print(f"Computer's final hand: {computer}, final score: {computer_score}")

        def replay():
            print(computer)
                      
            if player_score==computer_score:
                message()
                print("draw")

            elif player_score>computer_score and player_score<=21:
                message()
                print("You win")

            elif player_score<computer_score and computer_score>21:
                message()
                print("computer went over. You win")

            elif player_score<computer_score and player_score<21:
                message()
                print("You loss")

            elif player_score>computer_score and player_score>21:
                message()
                print("You went over. computer win")
            
            
            
        if player_score <= 21:
          
            print(f"Your cards: {player}, current score: {player_score}")
            print(f"Computer's first card: {computer[0]}")
            continue_play=input("Type 'y' to get another card, type 'n' to pass:")
            if continue_play =="y":
                for x in range(0,1):
                    computer_draw=random.randint(1,10)
                    player_draw=random.randint(1,10)
                    computer.append(computer_draw)
                    player.append(player_draw)                        
                    computer_score+=computer_draw
                    player_score+=player_draw

                    for x in range(len(computer)):
                        if computer[x]==1 and computer_score<21:
                            computer_score-=1
                            computer[x]=11
                            computer_score+=11
                            break
                    for x in range(len(player)):
                        if player[x]==1 and player_score<21:
                            player_score-=1
                            player[x]=11
                            player_score+=11
                            break
                            
                    
            elif continue_play=='n':
                if  computer_score<17:
                    while computer_score<17:
                        print("becouse computer final score is less than 17 it must have to draw another card")
                        computer_draw=random.randint(1,10)
                        computer.append(computer_draw)
                        computer_score+=computer_draw
                        for x in range(len(computer)):
                            if computer[x]==1 and computer_score<21:
                                computer_score-=1
                                computer[x]=11
                                computer_score+=11
                                break

                    replay()
                    loop2=False
                else:
                    replay()
                    loop2=False

                
        elif player_score>21:
            print("You went over. computer win")
            loop2=False

continue_play=True
while continue_play:
    
    play=input("Do you want to play a game of Blackjack? Type 'y' or 'n':" )
    if play=="y":
        os.system('cls')
        logo()
        black_jack()
        
    else:
        print="Thanks for playing"
        continue_play=False
    


