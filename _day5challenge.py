#PyPassword Generator!


letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password? coose frome 1 to 26 \n")) 
nr_symbols = int(input(f"How many symbols would you like? coose frome 1 to 9 \n"))
nr_numbers = int(input(f"How many numbers would you like? coose frome 1 to 10 \n"))

import random
store=[]
password_list=[]
password=""

for x in range(0,nr_letters):
    num1=random.randint(0,25)
    store.append(letters[num1])
for x in range(0,nr_symbols):
    num2=random.randint(0,8)
    store.append(symbols[num2])
for x in range(0,nr_numbers):
    num3=random.randint(0,9)
    store.append(numbers[num3])

length=len(store)
for y in range(0,length):
    possition=random.randint(0,length-1)
    password_list.append(store[possition])

for i in password_list:
    password += str(i) 
print(f"Your password is: {password}")
