from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
Coffee_maker = CoffeeMaker()

menu = Menu()
is_on = True

money_machine.report()
Coffee_maker.report()

while is_on:
    options = menu.get_items()
    choice = input(f"What would you like? {options}: ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        Coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if Coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
           
                Coffee_maker.make_coffee(drink)