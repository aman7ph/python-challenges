#prime number
def prime_checker(number):
    for x in range(2,number+1):
        if number%x==0:
            if x!=number:
                print("It's not a prime number.")
                break
            else:
                print("It's a prime number.")
                break


#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)