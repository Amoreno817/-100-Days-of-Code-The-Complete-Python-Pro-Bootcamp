# Coffee Machine Project
Menu = {
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
    }}
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
is_on = True
profit = 0

while is_on:
    user_input = input("What would you like? (espresso/latte/cappuccino): ").strip().lower()
    
    if user_input == "off":
        is_on = False
    elif user_input == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    elif user_input in Menu:
        drink = Menu[user_input]
        if resources["water"] < drink["ingredients"].get("water", 0):
            print("Sorry there is not enough water.")
        elif resources["milk"] < drink["ingredients"].get("milk", 0):
            print("Sorry there is not enough milk.")
        elif resources["coffee"] < drink["ingredients"].get("coffee", 0):
            print("Sorry there is not enough coffee.")
        else:
            print("Please insert coins.")
            try:
                quarters = int(input("how many quarters?: "))
                dimes = int(input("how many dimes?: "))
                nickles = int(input("how many nickles?: "))
                pennies = int(input("how many pennies?: "))
            except ValueError:
                print("Invalid input. Please enter integers only.")
                continue
            
            total = quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01
            if total < drink["cost"]:
                print("Sorry that's not enough money. Money refunded.")
            else:
                change = total - drink["cost"]
                profit += drink["cost"]
                resources["water"] -= drink["ingredients"].get("water", 0)
                resources["milk"] -= drink["ingredients"].get("milk", 0)
                resources["coffee"] -= drink["ingredients"].get("coffee", 0)
                print(f"Here is ${change:.2f} in change.")
                print(f"Here is your {user_input} ☕️. Enjoy!")
    else:
        print("Invalid input. Please try again.")