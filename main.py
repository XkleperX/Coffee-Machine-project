from menu import MENU
from art import logo,coin


print(logo)
resources = {"water": 300, "milk": 200, "coffee": 100, "money": 0}

quarter = 0.25
dimes = 0.10
nickel = 0.05
pennies = 0.01

should_stop = False

while not should_stop:

    drink = input("What would you like? (espresso/latte/cappuccino):")
    if drink == "report":
        format_water = f"Water: {resources['water']}ml \nMilk: {resources['milk']}ml \ncoffee: {resources['coffee']}ml \nMoney: {resources['money']}"
        print(format_water)
        should_stop = True

    elif drink == "espresso" or drink == "cappuccino" or drink == "latte":

        def order(drink):
            water = MENU[drink]["ingredients"]["water"]
            if drink == "cappuccino" or drink == "latte":
                milk = MENU[drink]["ingredients"]["milk"]
            else:
                milk = 0
            coffee = MENU[drink]["ingredients"]["coffee"]
            cost = MENU[drink]["cost"]

            return water, milk, coffee, cost

        water_drink = order(drink)[0]
        milk_drink = order(drink)[1]
        coffee_drink = order(drink)[2]
        cost_drink = order(drink)[3]

        def check_order(water, milk, coffee):
            if water > resources["water"]:
                print("you don't have enough water")
                return False
            elif milk > resources["milk"]:
                print("you don't have enough milk")
                return False

            elif coffee > resources["coffee"]:
                print("you don't have enough coffee")
                return False

            else:
                resources["water"] -= water
                resources["milk"] -= milk
                resources["coffee"] -= coffee
                return True

        if check_order(water_drink, milk_drink, coffee_drink):
            print(coin)
            print("please insert a coin first")

            no_quarter = int(input("how many quarters?: "))
            no_dimes = int(input("how many dimes?: "))
            no_nickel = int(input("how many nickel?: "))
            no_pennies = int(input("how many pennies?: "))

            cal = (
                quarter * no_quarter
                + dimes * no_dimes
                + nickel * no_nickel
                + pennies * no_pennies
            )

            your_change = cal - cost_drink
            if your_change <= 0:
                print("you don't have enough money")
                should_stop = True
            elif your_change >= cost_drink:
                resources["money"] += cost_drink
                print(f"Your total cost is: ${cost_drink:.2f}")
                print(f"Your change ${your_change:.2f} ")
                print(f"Thank you for ordering {drink}")
        else:
            should_stop = True
    else:
        print("Invalid data")
        should_stop = True