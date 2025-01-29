# Name: Ashley Chan
# Date: 09/27/2023
# Purpose: Driver Code for Contacts Module

from contacts import *

contacts = []

while (True):
    print("")
    print("      *** TUFFY TITAN CONTACT MAIN MENU\n")
    print("1. Add contact")
    print("2. Modify contact")
    print("3. Delete contact")
    print("4. Print contact list")
    print("5. Find Contact")
    print("6. Exit the program\n")
    menu_choice = int(input("Enter menu choice: "))
    print("")

    # Add contact
    if menu_choice == 1:
        id = int(input("Enter phone number: "))
        first_name = str(input("Please enter the contact's first name: "))
        last_name = str(input("Please enter the contact's last name: "))
        if id in contacts.keys():
            add_contact(contacts, id, first_name, last_name)
            print("Added: " + first_name + " " + last_name)
        else:
            print("Phone number already exists.")

    # Modify contacts
    elif menu_choice == 2:
        id = int(input("Enter phone number: "))
        index = int(input("Please enter the contact list index you would like to modify. "))
        first_name = str(input("Please enter the contact's first name: "))
        last_name = str(input("Please enter the contact's last name: "))
        if id in contacts.keys():
            modify_contact(contacts, id, first_name, last_name)
        else:
            print("Phone number does not exist.")
   
    # Delete Contact 
    elif menu_choice == 3:
        id = int(input("Enter phone number: "))
        if id in contacts.keys():
            modify_contact(contacts, id, first_name, last_name)
        else:
            print("Invalid phone number.")
   

    # Print sorted contact list
    elif menu_choice == 4:
        print("==================== CONTACT LIST ====================")
        print("Last Name             First Name            Phone     ")
        print("====================  ====================  ==========")
        for i in range (len(contacts)):
            print(f'{str(i):8}{contacts[i][1]:22}{contacts[i][0]:22}')
    
    # Find contact
    elif menu_choice == 5:
        sort_contacts(contacts, 0)

    # Quit Program
    elif menu_choice == 6:
        break
    else:
        "Sorry, that's an invalid menu choice. Try again."


