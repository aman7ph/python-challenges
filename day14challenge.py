#higher-lower
from art_and_data import day14challenge_art
from art_and_data import day14challenge_data
import random
import os
print(day14challenge_art.logo)
dict=day14challenge_data.data
score=0
fuck=True
while fuck:
    r1=random.randint(0,49)
    r2=random.randint(0,49)
    print(f"Compare A: {dict[r1]['name']}, a {dict[r1]['description']}, from {dict[r1]['country']}.")
    print(dict[r1]['follower_count'])
    print(day14challenge_art.vs)
    print(f"Against B: {dict[r2]['name']}, a {dict[r2]['description']}, from {dict[r2]['country']}.")
    print(dict[r2]['follower_count'])

    AorB=input("Who has more followers? Type 'A' or 'B':").lower()
    
    A=dict[r1]['follower_count']
    B=dict[r2]['follower_count']

    if A>B and AorB=='a':
        os.system('cls')
        score+=1
        print(f"You're right! Current score: {score}")
    elif A<B and AorB=='a':
        print(f"Sorry, that's wrong. Final score: {score}")
        fuck=False
    elif B>A and AorB=='b':
        os.system('cls')
        score+=1
        print(f"You're right! Current score: {score}")
    elif B<A and AorB=='b':
        print(f"Sorry, that's wrong. Final score: {score}")
        fuck=False      
            
        







