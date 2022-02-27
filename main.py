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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
money = [0]


def report():
    """prints the current resource balance and money received so far"""
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${money[0]}")


def check_resources(drink):
    """see if enough resources for the drink are available.
    If not, print which are the resources not enough to make the drink"""
    req_water = 0
    req_milk = 0
    req_coffee = 0
    cost = 0
    curr_water = resources["water"]
    curr_milk = resources["milk"]
    curr_coffee = resources["coffee"]

    for item in MENU:
        if drink == "espresso" and item == drink:
            req_water = MENU[item]["ingredients"]["water"]
            req_coffee = MENU[item]["ingredients"]["coffee"]
            cost = MENU[item]["cost"]
        elif drink != "espresso" and item == drink:
            req_water = MENU[item]["ingredients"]["water"]
            req_milk = MENU[item]["ingredients"]["milk"]
            req_coffee = MENU[item]["ingredients"]["coffee"]
            cost = MENU[item]["cost"]

    if req_water <= curr_water and req_milk <= curr_milk and req_coffee <= curr_coffee:
        have_resource = True
        print(f"It will cost you ${MENU[drink]['cost']}")
    else:
        have_resource = False
        if req_water > curr_water:
            print("Sorry, there is no enough water")
        if req_milk > curr_milk:
            print("Sorry, there is no enough milk")
        if req_coffee > curr_coffee:
            print("Sorry, there is no enough coffee")
    return have_resource, cost, req_water, req_milk, req_coffee


def deliver_drink(drink, wat, mil, coff):
    """update resources after delivering the drink"""
    print(f"Here is your {drink} ☕. Enjoy!")
    resources["water"] = resources["water"] - wat
    resources["milk"] = resources["milk"] - mil
    resources["coffee"] = resources["coffee"] - coff


def check_money(cost, drink, water_amount, milk_amount, coffee_amount):
    """Check if the user has given enough money to buy the drink.
    Money is calculated to US dollars.
    Machine accepts money as quarters, dimes, nickel and pennies.
    Calculate and give if any balance amount needs to be given back to user."""
    quarters = int(input("how many quarters? "))
    dimes = int(input("how many dimes? "))
    nickels = int(input("how many nickels? "))
    pennies = int(input("how many pennies? "))

    user_money = quarters * 0.25 + dimes * 0.1 + nickels * 0.05 + pennies * 0.01
    if user_money >= cost:
        money[0] = cost + money[0]
        if user_money > cost:
            balance = user_money - cost
            print(f"Here is ${balance} in change")
            deliver_drink(drink, water_amount, milk_amount, coffee_amount)

    else:
        print("Sorry that's not enough money. Money refunded")


# Input generation
while True:
    user_input = input("What would you like? (espresso/latte/cappuccino):").lower()
    if user_input == "off":
        break
    elif user_input == "report":
        report()
    elif user_input == "espresso" or "latte" or "cappuccino":
        res_status, drink_cost, water, milk, coffee = check_resources(user_input)
        if res_status:
            check_money(drink_cost, user_input, water, milk, coffee)
