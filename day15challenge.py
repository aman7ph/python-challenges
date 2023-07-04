""" 
espresso /1.5$ /50ml water 18g coff    
late /2.5$   /2ooml water 24g coffee  150 ml milk
 cappuccino /3.0$ /250ml water 24g coffy 100ml milk
 penny = 0.01$
 nickels=0.05$
 dime=0.1$
quarter=0.25$"""

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def coffi_machin(chooice):
      print("Please insert coins.")
      quarters=float(input("how many quarters?:  "))*0.25
      dimes=float(input("how many dimes?:  "))*0.1
      nickles=float(input("how many nickles?:  "))*0.05
      pennies=float(input("how many pennies?:  "))*0.01
      money=quarters+dimes+nickles+pennies
      print(money)
      if chooice =='espresso':
          if money>=1.5:
              if resources['water']>=50:
                  resources['water']-=50
                  if resources['coffee']>=18:
                    resources['coffee']-=18
                    change=money-1.5
                    global profit
                    profit+=1.5
                    print(f"Here is $ {change} in change.")
                    print("Here is your espresso ☕️. Enjoy!")

                  else:
                    print("Sorry there is not enough coffee.")

              else:
                print("Sorry there is not enough water.")

          
          else:
              print("Sorry that's not enough money. Money refunded  {money}$.")
      if chooice =='late':
          if money>=2.5:
              if resources['water']>=200:
                  resources['water']-=200
                  if resources['coffee']>=24:
                    resources['coffee']-=24
                    if resources['milk']>=150:
                      resources['milk']-=150
                      change=money-2.5
                      global profit
                      profit+=2.5
                      print(f"Here is $ {change} in change.")
                      print("Here is your late ☕️. Enjoy!")
                    else:
                      print("Sorry there is not enough milk.")
                  else:
                    print("Sorry there is not enough coffee.")

              else:
                print("Sorry there is not enough water.")          
          else:
              print("Sorry that's not enough money. Money refunded  {money}$.")
      if chooice =='cappuccino':
        if money>=3:
            if resources['water']>=250:
                resources['water']-=250
                if resources['coffee']>=24:
                  resources['coffee']-=24
                  if resources['milk']>=100:
                    resources['milk']-=100
                    change=money-3
                    global profit
                    profit+=3
                    print(f"Here is $ {change} in change.")
                    print("Here is your cappuccino ☕️. Enjoy!")
                  else:
                     print("Sorry there is not enough milk.")

                else:
                  print("Sorry there is not enough coffee.")

            else:
              print("Sorry there is not enough water.")

          
        else:
            print("Sorry that's not enough money. Money refunded  {money}$.")
    
love=True
while love: 
  type_name=input("What would you like? (espresso/latte/cappuccino):   ")
  if type_name=="off":
    love=False
    print("shuting down")
  elif type_name=="report":
    print(f"Water : {resources['water']} ml")
    print(f"Milk : {resources['milk']} ml")
    print(f"Coffee : {resources['coffee']} gm")
    print(f"Money : {profit} $")
  else:
    coffi_machin(type_name)









