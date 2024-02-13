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
    },
}
resources = {"water": 300, "milk": 200, "coffee": 100, "money": 0}

drink = input("What would you like? (espresso/latte/cappuccino):")
if drink == "report":
    print(
        f"Water: {resources['water']}ml \nMilk: {resources['milk']}ml \ncoffee: {resources['coffee']}ml \nMoney: {resources['money']}"
    )




#! I need to get the order and get the amount of the wasted resources

    
#! or I can use the drink as this Menu["Drink"]["cost"] and save every thing done
    


def order(drink):
    water = MENU[drink]["ingredients"]["water"]
    milk = MENU[drink]["ingredients"]["milk"]
    coffee = MENU[drink]["ingredients"]["coffee"]
    cost = MENU[drink]["cost"]

    return water,milk,coffee,cost

print(order(drink))


water_drink=order(drink)[0]
milk_drink= order(drink)[1]
coffee_drink= order(drink)[2]
cost_drink= order(drink)[3]

def check_order (water,milk,coffee,cost):
    if water > resources["water"]:
        print("you don't have enough water")
    elif milk > resources["milk"]:
        print("you don't have enough milk")
    elif coffee > resources["coffee"]:
        print("you don't have enough coffee")
    elif money_count()<cost:
        print("you don't have enough money")


check_order(water=water_drink,milk=milk_drink,coffee=coffee_drink,cost=cost_drink)




print("please insert a coin first")
quarter = 0.25
dimes = 0.10
nickel = 0.05
pennies = 0.01

no_quarter = int(input("how many quarters?: "))
no_dimes = int(input("how many dimes?: "))
no_nickel = int(input("how many nickel?: "))
no_pennies = int(input("how many pennies?: "))

def money_count():

    cal = (
        quarter * no_quarter
        + dimes * no_dimes
        + nickel * no_nickel
        + pennies * no_pennies
    )
    return cal
