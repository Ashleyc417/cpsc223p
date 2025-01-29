# Name: Ashley Chan
# Date: 08/30/2023
# File Purpose: Tuffy Titan Contact List Driver

from contacts import *

contact_list = []

while (True):
    print("")
    print("      *** TUFFY TITAN CONTACT MAIN MENU\n")
    print("1. Print list")
    print("2. Add contact")
    print("3. Modify contact")
    print("4. Delete contact")
    print("5. Exit the program\n")
    menu_choice = int(input("Enter menu choice: "))
    print("")

    if menu_choice == 1:
        print_list(contact_list)
    elif menu_choice == 2:
        add_contact(contact_list)
    elif menu_choice == 3:
        modify_contact(contact_list)
    elif menu_choice == 4:
        delete_contact(contact_list)
    elif menu_choice == 5:
        break
    else:
        "Sorry, that's an invalid menu choice. Try again."
