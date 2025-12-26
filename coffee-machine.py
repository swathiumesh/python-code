# Coffee Machine Program

# Define drink recipes (water, milk, coffee, cost)
MENU = {
    "espresso": {
        "water": 50,
        "milk": 0,
        "coffee": 18,
        "cost": 1.50
    },
    "latte": {
        "water": 200,
        "milk": 150,
        "coffee": 24,
        "cost": 2.50
    },
    "cappuccino": {
        "water": 250,
        "milk": 100,
        "coffee": 24,
        "cost": 3.00
    }
}

# Machine resources
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0.0
}


def print_report():
    """Display current machine resources and money."""
    print("\n--- Machine Report ---")
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${resources['money']:.2f}\n")


def check_resources(drink):
    """Check if machine has enough resources for the selected drink."""
    recipe = MENU[drink]
    
    if resources["water"] < recipe["water"]:
        print("Sorry there is not enough water.")
        return False
    elif resources["milk"] < recipe["milk"]:
        print("Sorry there is not enough milk.")
        return False
    elif resources["coffee"] < recipe["coffee"]:
        print("Sorry there is not enough coffee.")
        return False
    
    return True


def process_coins():
    """Process coin input and return total money inserted."""
    print("\nPlease insert coins.")
    quarters = int(input("How many quarters? "))
    dimes = int(input("How many dimes? "))
    nickels = int(input("How many nickels? "))
    pennies = int(input("How many pennies? "))
    
    total = quarters * 0.25 + dimes * 0.10 + nickels * 0.05 + pennies * 0.01
    return round(total, 2)


def check_transaction(drink, money_inserted):
    """Check if transaction is successful and handle change."""
    cost = MENU[drink]["cost"]
    
    if money_inserted < cost:
        print(f"Sorry that's not enough money. Money refunded.")
        return False
    
    # Transaction successful: add cost to machine money
    resources["money"] += cost
    
    # Handle change
    if money_inserted > cost:
        change = round(money_inserted - cost, 2)
        print(f"Here is ${change:.2f} dollars in change.")
    
    return True


def make_drink(drink):
    """Deduct resources and serve the drink."""
    recipe = MENU[drink]
    resources["water"] -= recipe["water"]
    resources["milk"] -= recipe["milk"]
    resources["coffee"] -= recipe["coffee"]
    print(f"Here is your {drink}. Enjoy!\n")


def main():
    """Main coffee machine loop."""
    print("☕ Welcome to the Coffee Machine! ☕\n")
    
    while True:
        choice = input("What would you like? (espresso/latte/cappuccino): ").lower().strip()
        
        if choice == "off":
            print("Machine turning off. Goodbye!")
            break
        elif choice == "report":
            print_report()
        elif choice in MENU:
            if check_resources(choice):
                money_inserted = process_coins()
                if check_transaction(choice, money_inserted):
                    make_drink(choice)
        else:
            print("Invalid choice. Please enter espresso, latte, cappuccino, report, or off.\n")


if __name__ == "__main__":
    main()
