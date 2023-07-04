###############################

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

def check_resource(item_name):
        ingredent=MENU[item_name]['ingredients']
        for item in ingredent:
            if resources[item]>=ingredent[item]:
                return True
            else:
                return False
def check_money():
        print("Please insert coins.")
        quarters=float(input("how many quarters?:  "))*0.25
        dimes=float(input("how many dimes?:  "))*0.1
        nickles=float(input("how many nickles?:  "))*0.05
        pennies=float(input("how many pennies?:  "))*0.01
        money=quarters+dimes+nickles+pennies
        print(money)
        return money
def make_coffy(item_name):
        ingredent=MENU[item_name]['ingredients']
        money=check_money()
        cost=MENU[item_name]['cost']
        if money>=cost:
            if check_resource(item_name):
                for item in ingredent:                    
                    resources[item]-=ingredent[item]                
                money-=cost
                global profit
                profit+=cost
                print(f"Here is $ {money} in change.")
                print(f"Here is your {item_name} ☕️. Enjoy!")
            else:
                print(f"Sorry there is not enough resourse. Money refunded  {money}$")
                return False
        else:
            print(f"Sorry that's not enough money. Money refunded  {money}$.")
        
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
    make_coffy(type_name)
    


        
