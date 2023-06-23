import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

drlist=[rock,paper,scissors]
ran=random.randint(0,len(drlist)-1)
choose=int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
if choose==0 and ran==0:
    print(drlist[0])
    print("commputer coice")
    print(drlist[0])
    print("draw")
elif choose==0 and ran==1:
    print(drlist[0])
    print("commputer coice")
    print(drlist[1])
    print("you lose")
elif choose==0 and ran==2:
    print(drlist[0])
    print("commputer coice")
    print(drlist[2])
    print("you winn")
elif choose==1 and ran==0:
    print(drlist[0])
    print("commputer coice")
    print(drlist[0])
    print("you winn")
elif choose==1 and ran==1:
    print(drlist[0])
    print("commputer coice")
    print(drlist[1])
    print("draw")
elif choose==1 and ran==2:
    print(drlist[0])
    print("commputer coice")
    print(drlist[2])
    print("you loss")
elif choose==2 and ran==0:
    print(drlist[0])
    print("commputer coice")
    print(drlist[0])
    print("you loss")
elif choose==2 and ran==1:
    print(drlist[0])
    print("commputer coice")
    print(drlist[1])
    print("you winn")
elif choose==2 and ran==2:
    print(drlist[0])
    print("commputer coice")
    print(drlist[2])
    print("draw")
