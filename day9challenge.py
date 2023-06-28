#blind-auction

import os
from art_and_data import day9challenge_Art
logo=day9challenge_Art.logo

print(logo)

name=input("What is your name?:\t").lower()
bid=int(input("What is your bid?:\t$"))


auction={}
winer_name=" "

def adding_auction(name,bid): 
    bid_max=0
    index=0
    readd=True
    while readd:  
        
        rego=input("Are there any other bidders? Type 'yes or 'no'.").lower()
        if rego !='yes':
            readd=False
        else:
            os.system('cls')
            name=input("What is your name?:\t").lower()
            bid=int(input("What is your bid?:\t$"))
            auction[index]={}
            auction[index]["name"]=name
            auction[index]["bid"]=bid
        index+=1
        

    for x in auction:
        if auction[x]["bid"]>bid_max:
            bid_max=auction[x]["bid"]
            winer_name=auction[x]["name"]

    return f"The winner is {winer_name} with a bid of ${bid_max}"


print(adding_auction(name,bid))



