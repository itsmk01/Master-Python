import os

def clear():
    # For Windows
    if os.name == 'nt':
        os.system('cls')
    # For Mac and Linux (name is 'posix')
    else:
        os.system('clear')

# Example usage


MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk" : 0,
            "coffee": 18,
        },
        "cost": 50,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 150,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 180,
    }
}

resources = {
    "water": 1000,
    "milk": 600,
    "coffee": 100,
}


def update_resources(water_used, milk_used, coffee_used) :
    resources["water"] -= water_used
    resources["milk"] -= milk_used
    resources["coffee"] -= coffee_used
    

def resources_left() :
    water_left = resources["water"]
    milk_left = resources["milk"]
    coffee_left = resources["coffee"]
    print(f"Water : {water_left}")
    print(f"Milk : {milk_left}")
    print(f"Coffee : {coffee_left}")
    return (water_left + milk_left + coffee_left)


def check_resources(item, flavour) :
    #for item in MENU[flavour]["ingredients"] :
    if resources[item] < MENU[flavour]["ingredients"][item] :
        return False
    return True


def calculate_change(flavour, note100_used, note50_used, note20_used, note10_used) :
    money_collected = float((note100_used*100) + (note50_used*50) + (note20_used*20) + (note10_used*10))
    change = money_collected - MENU[flavour]["cost"]
    return change


switch = "on"
while switch == "on" :
    
    choice = input("What would you like? (espresso/latte/cappuccino) ").lower()

    if choice == "report" :
        resources_left()
        continue

    print("Please insert Note's : ")
    note100 = float(input("How many ₹100 Notes ? "))
    note50 = float(input("How many ₹50 Notes ? "))
    note20 = float(input("How many ₹20 Notes ? "))
    note10 = float(input("How many ₹10 Notes ? "))

    change = round(calculate_change(flavour=choice, note100_used=note100, note50_used=note50, note20_used=note20, note10_used=note10), 2)
    
    if change < 0 :
        clear()
        print("You don't have enough money .")
        continue


    if choice == "espresso" :
        if not check_resources(item="water", flavour=choice):
            clear()
            print(f"Sorry there is not enough water. Your Money will be refunded.")
            continue
        elif not check_resources(item="milk", flavour=choice):
            clear()
            print(f"Sorry there is not enough milk. Your Money will be refunded.")
            continue
        elif not check_resources(item="coffee", flavour=choice):
            clear()
            print(f"Sorry there is not enough coffee. Your Money will be refunded.")
            continue
        update_resources(water_used=MENU["espresso"]["ingredients"]["water"] ,milk_used=MENU["espresso"]["ingredients"]["milk"] , coffee_used=MENU["espresso"]["ingredients"]["coffee"])
    elif choice == "latte" :
        if not check_resources(item="water", flavour=choice):
            clear()
            print(f"Sorry there is not enough water. Your Money will be refunded.")
            continue
        elif not check_resources(item="milk", flavour=choice):
            clear()
            print(f"Sorry there is not enough milk. Your Money will be refunded.")
            continue
        elif not check_resources(item="coffee", flavour=choice):
            clear()
            print(f"Sorry there is not enough coffee. Your Money will be refunded.")
            continue
        update_resources(water_used=MENU["latte"]["ingredients"]["water"], milk_used=MENU["latte"]["ingredients"]["milk"], coffee_used=MENU["latte"]["ingredients"]["coffee"])
    elif choice == "cappuccino" :
        if not check_resources(item="water", flavour=choice):
            clear()
            print(f"Sorry there is not enough water. Your Money will be refunded.")
            continue
        elif not check_resources(item="milk", flavour=choice):
            clear()
            print(f"Sorry there is not enough milk. Your Money will be refunded.")
            continue
        elif not check_resources(item="coffee", flavour=choice):
            clear()
            print(f"Sorry there is not enough coffee. Your Money will be refunded.")
            continue
        update_resources(water_used=MENU["cappuccino"]["ingredients"]["water"], milk_used=MENU["cappuccino"]["ingredients"]["milk"], coffee_used=MENU["cappuccino"]["ingredients"]["coffee"])
    

    print(f"Here is ₹{change} in change. ")
    print(f"Here is your {choice} ☕. Enjoy ! ")


    switch = input("On or Off Coffee Machine : ").lower()
    clear()

 


    

