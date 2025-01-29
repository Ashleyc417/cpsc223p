# Name: Ashley Chan
# Date: 09/13/2023
# Purpose: Driver Code for Contacts Module

from contacts import *

contact_list = []

while (True):
    print("")
    print("      *** TUFFY TITAN CONTACT MAIN MENU\n")
    print("1. Print list")
    print("2. Add contact")
    print("3. Modify contact")
    print("4. Delete contact")
    print("5. Sort list by first name")
    print("6. Sort list by last name")
    print("7. Exit the program\n")
    menu_choice = int(input("Enter menu choice: "))
    print("")

    # Print each individual contact index, first, and last name
    if menu_choice == 1:
        for i in range (len(contact_list)):
            print(f'{str(i):8}{contact_list[i][0]:22}{contact_list[i][1]:22}')
    
    # Add contact
    elif menu_choice == 2:
        first_name = str(input("Please enter the contact's first name: "))
        last_name = str(input("Please enter the contact's last name: "))
        add_contact(contact_list, first_name, last_name)

    # Modify contact_list
    elif menu_choice == 3:
        index = int(input("Please enter the contact list index you would like to modify. "))
        first_name = str(input("Please enter the contact's first name: "))
        last_name = str(input("Please enter the contact's last name: "))
        modify_contact(contact_list, first_name, last_name, index)
   
    # Delete Contact 
    elif menu_choice == 4:
        index = int(input("Please enter the contact list index you would like to delete. "))
        delete_contact(contact_list, index)

    # Sort Contacts by First Name
    elif menu_choice == 5:
        sort_contacts(contact_list, 0)

    # Sort Contacts by Last Name
    elif menu_choice == 6:
        sort_contacts(contact_list, 1)

    # Quit Program
    elif menu_choice == 7:
        break
    else:
        "Sorry, that's an invalid menu choice. Try again."


