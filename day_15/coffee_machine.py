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
money = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def print_report(coins):
    print(f"Water: {resources['water']}ml\n"
          f"Milk: {resources['milk']}ml\n"
          f"Coffee: {resources['coffee']}g\n"
          f"Money: ${coins}")


def check_resources(ingredients):
    for ingredient in ingredients:
        if resources[ingredient] < ingredients[ingredient]:
            print(f"Sorry, there is not enough {ingredient}")
            return False
    return True


def get_coins():
    print("Please insert coins.")
    total = int(input("How many quarters?  ")) * 0.25
    total += int(input("How many dimes?  ")) * 0.1
    total += int(input("How many nickles?  ")) * 0.05
    total += int(input("How many pennies?  ")) * 0.01
    return total


def check_total(total_received):
    if total_received < drink['cost']:
        print("Sorry, that's not enough money. Money refunded.")
        return False
    else:
        global money
        money += drink['cost']
        total_received = round(total_received - drink['cost'], 2)
        print(f"Here is ${total_received} in change.")
        print(f"Here is your {choice}. ☕ Enjoy!")
        return True


def update_resources(used):
    for ingredient in used:
        resources[ingredient] -= used[ingredient]


is_machine_on = True

while is_machine_on:
    choice = input("What would you like? (espresso/latte/cappuccino):  ")
    if choice == 'report':
        print_report(money)
    elif choice == 'off':
        is_machine_on = False
    else:
        drink = MENU[choice]
        enough_resources = check_resources(drink['ingredients'])
        if enough_resources:
            coin_total = get_coins()
            enough_money = check_total(coin_total)
            if enough_money:
                update_resources(drink['ingredients'])



