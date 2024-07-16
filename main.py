# imports

from time import sleep
from art import logo
from art import separator

# imports end

# constants

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

# constants end

# global variables

on = True
beverage = ""
profit = 0

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

status = f"""
profit: ${profit}
coffee: {resources["coffee"]}g
water: {resources["water"]}ml
milk: {resources["milk"]}ml
"""

# global variables end

# functions


def choose_beverage():
    global beverage
    beverage = input("Choose beverage: (1 - Espresso, 2 - Cappuccino, 3 - Latte)\n")

    if beverage == "report":
        print(status)
        sleep(8)
        choose_beverage()

    elif beverage == "resupply":
        resupply()
        interface()
        choose_beverage()

    elif int(beverage) == 1:
        beverage = "espresso"

    elif int(beverage) == 2:
        beverage = "cappuccino"

    elif int(beverage) == 3:
        beverage = "latte"

    else:
        interface()
        choose_beverage()


def check_resources(resources_needed_to_make):
    global beverage
    for item in resources_needed_to_make:
        if resources[item] < resources_needed_to_make[item]:
            beverage = item
            return False
        else:
            return True


def payment():
    global beverage, profit
    print(f"\nCost: ${resources_needed["cost"]}\n")
    money_given = check_coins()
    if money_given == resources_needed["cost"]:
        print(f"Paid exactly!\n")
        profit = resources_needed["cost"]
        return True
    elif money_given > resources_needed["cost"]:
        print(f"Change: {money_given - resources_needed["cost"]}\n")
        profit = resources_needed["cost"]
        return True
    else:
        print(f"You fell short by {resources_needed["cost"] - money_given}. Try again!")
        if input("Wanna try again? (y/n)").lower() == "y":
            payment()
        else:
            return False


def check_coins():
    total = 0
    total += round(0.25 * int(input("Insert quarters\n")), 2)
    if total >= resources_needed["cost"]:
        return total
    print(f"Your current total is: ${total}\n{round(resources_needed["cost"] - total, 2)} left")
    total += round(0.10 * int(input("Insert dimes\n")), 2)
    if total >= resources_needed["cost"]:
        return total
    print(f"Your current total is: ${total}\n{round(resources_needed["cost"] - total, 2)} left")
    total += round(0.05 * int(input("Insert nickels\n")), 2)
    if total >= resources_needed["cost"]:
        return total
    print(f"Your current total is: ${total}\n{round(resources_needed["cost"] - total, 2)} left")
    total += round(0.01 * int(input("Insert pennies\n")), 2)
    return total


def make_coffee():
    global beverage
    print(f"Please wait while we make your {beverage}!\n")
    use_ingredients()
    for i in range(10):
        print("*  ", end=" ", flush=True)
        sleep(1)
    sleep(1.7)
    print("\033c", end="", flush=True)
    print(f"\n\nYour {beverage} is ready! Enjoy it :)")

    sleep(7)


def use_ingredients():
    global beverage
    ingredients_to_be_used = MENU[beverage]["ingredients"]
    for item in ingredients_to_be_used:
        resources[item] -= ingredients_to_be_used[item]


def resupply():
    for item in resources:
        resources[item] += int(input(f"resupplying {item}: "))
    if input("Do you want to keep resupplying? (y/n)").lower() == "y":
        resupply()
    else:
        return


def interface():
    print("\033c", end="", flush=True)
    print(logo)
    print(separator + "\n")


# functions end

# program

while on:
    interface()
    choose_beverage()
    resources_needed = MENU[beverage]
    if check_resources(resources_needed["ingredients"]):
        if payment():
            make_coffee()
    else:
        print(f"Sorry, there is not enough {beverage}")
        sleep(7)
        continue

# program end
