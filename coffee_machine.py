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


def calculate_change(flavour, quarters_used, dimes_used, nickles_used, pennies_used) :
    money_collected = float((quarters_used*0.25) + (dimes_used*0.10) + (nickles_used*0.05) + (pennies_used*0.01))
    change = money_collected - MENU[flavour]["cost"]
    return change

# water_used = 0
# milk_used = 0
# coffee_used = 0

choice = input("What would you like? (espresso/latte/cappuccino) ").lower()

if choice == "report" :
    resources_left()
if choice == "espresso" :
    update_resources(water_used=MENU["espresso"]["ingredients"]["water"], coffee_used=MENU["espresso"]["ingredients"]["coffee"])
elif choice == "latte" :
    update_resources(water_used=MENU["latte"]["ingredients"]["water"], milk_used=MENU["latte"]["ingredients"]["milk"], coffee_used=MENU["latte"]["ingredients"]["coffee"])
elif choice == "cappuccino" :
    update_resources(water_used=MENU["cappuccino"]["ingredients"]["water"], milk_used=MENU["cappuccino"]["ingredients"]["milk"], coffee_used=MENU["cappuccino"]["ingredients"]["coffee"])

print("Please insert coin's : ")
quarters = float(input("How many quarters ? "))
dimes = float(input("How many dimes ? "))
nickles = float(input("How many nickles ? "))
pennies = float(input("How many pennies ? "))

change = round(calculate_change(flavour=choice, quarters_used=quarters, dimes_used=dimes, nickles_used=nickles, pennies_used=pennies), 2)
print(f"Here is ${change} in change. ")

 


    

