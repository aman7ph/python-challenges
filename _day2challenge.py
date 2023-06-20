#tip calculator
#Write your code below this line 👇
print("Welcome to the tip calculator!")
total = float(input("What was the total bill? $\t"))
t_persent =int(input("How much tip would you like to give? 10, 12, or 15?\t"))
persent=t_persent/100
person=int(input("How many people to split the bill?\t"))
tip=total*persent
total_bill=total+tip
for_each_person=total_bill/person
rounding=round(for_each_person,2)
print(f"Each person should pay: ${rounding}")