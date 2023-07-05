from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine=MoneyMachine()
coffee_maker=CoffeeMaker()
menu=Menu()
love=True
while love:
    option = menu.get_items()
    choise=input(f"wich drink do you want ({option}) : ")
    if choise=="off":
        love=False
    elif choise=="report":
        money_machine.report()
        coffee_maker.report()
    else:
        drink=menu.find_drink(choise)
        if coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
            

        

