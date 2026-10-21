# ***************************************************************************
#
# Author: Paul Littrell & Adolfo Garcia
# Lab:    CIS-133Y Lab5 - Camping Gear Inventory Manager
# Date:   October 21, 2026
# Desc:   Main driver program for the Camping Gear Inventory. Displays a menu,
#         validates user input , and imports modular functions to add, edit,
#         delete, and display inventory items.
#
# Input:  Menu choices, gear item names, and item quantities.
# Output: Formatted camping gear inventory list and success/error messages.
# Source: Module 5 Lab
# GitHub: https://github.com/plittrell-pcc/CIS-133Y-Lab5
#
# ***************************************************************************

import module1 as m1  # PL: Added module for adding and editing items
import module2 as m2  # To be added by partner

def print_welcome_message():
    print("===========================================================")
    print("            CAMPING GEAR & SUPPLY CHECKLIST                ")
    print("===========================================================")
    print("This program helps you manage your camping gear inventory  ")
    print("by adding, editing, viewing, and removing checklist items. ")
    print("                                                           ")
    print("Please follow the prompts below to get started!          \n")
    print("-----------------------------------------------------------\n")


def display_menu():
    print("--- MAIN MENU ---\n")
    print("1. View Current Gear List")
    print("2. Add New Gear Item")
    print("3. Edit Existing Gear Item")
    print("4. Delete Gear Item")
    print("5. Quit Program")


def main():
    print_welcome_message()

    # Initial dictionary data storing gear items and quantities
    gear_inventory = {
        "Tent": 1,
        "Sleeping Bag": 2,
        "Camp Stove": 1,
        "Water Filter": 1
    }

    while True:
        display_menu()
        choice = m2.get_menu_choice()

        if choice == 1:
            # Needs to be added from Module 2
            m2.display_inventory(gear_inventory)

        elif choice == 2:
            # PL: Call module1 add function
            m1.add_item(gear_inventory)

        elif choice == 3:
            # PL: Call module1 edit function
            m1.edit_item(gear_inventory)

        elif choice == 4:
            # Needs to be added from Module 2
            m2.delete_item(gear_inventory)

        elif choice == 5:
            print("\nThank you for using the Camping Gear Inventory. Safe travels!")
            break


if __name__ == "__main__":
    main()