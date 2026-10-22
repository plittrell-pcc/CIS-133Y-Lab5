# ****************************************************************************
#
# Author: Adolfo Garcia
# Lab:    CIS-133Y Lab5 - Camping Gear Inventory Manager
# Date:   October 21, 2026
# Desc:   Module 2 containing menu validation, display formatting, and deletion
#         functions for the camping gear inventory dictionary.
#
# ****************************************************************************

def get_menu_choice():
    # Ask user for a menu option and make sure it's valid
    while True:
        try:
            choice = int(input("\nChoose an option (1-5): "))
            if 1 <= choice <= 5:
                return choice
            else:
                print("Please pick a number between 1 and 5.")
        except ValueError:
            print("That's not a number. Try again.")


def display_inventory(inventory):
    # Shows everything currently in the inventory
    print("\n--- Current Gear Inventory ---")

    if not inventory:
        print("No items yet.\n")
        return

    for item, qty in inventory.items():
        print(f"{item}: {qty}")
    print()  # spacing


def delete_item(inventory):
    print("\n--- Delete Gear Item ---")

    if not inventory:
        print("Nothing to delete. Inventory is empty.\n")
        return

    print("Items:")
    for item, qty in inventory.items():
        print(f"{item}: {qty}")
    print()

    # Asks for item name
    while True:
        name = input("Enter the item to delete: ").strip().title()
        if name in inventory:
            break
        print("That item doesn't exist. Try again.")

    # Asks for quantity to delete
    while True:
        try:
            amount = int(input(f"How many '{name}' do you want to delete? "))
            if amount > 0:
                break
            print("Enter a number greater than zero.")
        except ValueError:
            print("That's not a number. Try again.")

    # Makes sure they aren't deleting more than exists
    if amount > inventory[name]:
        print(f"You only have {inventory[name]} '{name}'. Can't delete {amount}.")
        return

    # Subtracts the amount
    inventory[name] -= amount

    # Removes item if quantity hits zero
    if inventory[name] == 0:
        del inventory[name]
        print(f"Removed all '{name}' from the inventory.\n")
    else:
        print(f"Deleted {amount} '{name}'. New quantity: {inventory[name]}\n")
