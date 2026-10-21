# ****************************************************************************
#
# Author: Paul Littrell
# Lab:    CIS-133Y Lab5 - Camping Gear Inventory Manager
# Date:   October 21, 2026
# Desc:   Module 1 containing input validation, addition, and editing functions
#         for the camping gear inventory dictionary.
#
# ****************************************************************************

def add_item(inventory):
    print("\n--- Add New Gear Item ---")

    # ADDED PL - Validate item name input
    while True:
        name = input("Enter gear item name: ").strip().title()
        if name:
            if name in inventory:
                print(f"Notice: '{name}' is already in the inventory.")
            break
        print("Error: Item name cannot be empty.")

    # ADDED PL - Validate quantity input
    while True:
        try:
            quantity = int(input(f"Enter quantity for '{name}': "))
            if quantity > 0:
                break
            print("Error: Quantity must be greater than zero.")
        except ValueError:
            print("Error: Invalid input. Please enter a whole number.")

    inventory[name] = quantity
    print(f"\n-> Success: Added {quantity} '{name}'(s) to inventory.\n")


def edit_item(inventory):
    print("\n--- Edit Existing Gear Item ---")

    if not inventory:
        print("Inventory is empty. Nothing to edit.\n")
        return

    # ADDED PL - Display current items using a loop for easy reference
    print("Current Items:")
    for item, qty in inventory.items():
        print(f" - {item}: {qty}")
    print()

    while True:
        name = input("Enter the exact name of the item you want to edit: ").strip().title()
        if name in inventory:
            break
        print(f"Error: '{name}' not found in inventory. Please try again.")

    # ADDED PL - Validate new quantity
    while True:
        try:
            new_qty = int(input(f"Enter new quantity for '{name}' (current: {inventory[name]}): "))
            if new_qty > 0:
                break
            print("Error: Quantity must be greater than zero.")
        except ValueError:
            print("Error: Invalid input. Please enter a whole number.")

    inventory[name] = new_qty
    print(f"\n-> Success: Updated '{name}' quantity to {new_qty}.\n")