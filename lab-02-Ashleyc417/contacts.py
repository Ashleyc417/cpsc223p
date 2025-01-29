# Name: Ashley Chan
# Date: 08/30/2023
# File Purpose: Tuffy Titan Contact List Functionality

# contact_list: [["first name, last name"], ["first name, last time"], ...]

def print_list(contact_list):
    """
    This function will print a given contact list.
    """

    #Print each individual contact index, first, and last name
    for i in range (len(contact_list)):
         print(f'{str(i):8}{contact_list[i][0]:22}{contact_list[i][1]:22}')

def add_contact(contact_list):
    """
    This function will add a contact.
    """
    first_name = str(input("Please enter the contact's first name: "))
    last_name = str(input("Please enter the contact's last name: "))
    contact = [first_name, last_name]
    contact_list.append(contact)
    return contact_list

def modify_contact(contact_list):
    """
    This function will modify a contact.
    """
    index = int(input("Please enter the contact list index you would like to modify. "))
    if index not in range(len(contact_list)):
        print("Invalid index number.")
        return contact_list

    first_name = str(input("Please enter the contact's first name: "))
    last_name = str(input("Please enter the contact's last name: "))
    contact_list[index] = [first_name, last_name]
    return contact_list

def delete_contact(contact_list):
    """
    This function will delete a contact.
    """
    index = int(input("Please enter the list index you would like to modify. "))
    if index not in range(len(contact_list)):
        print("Invalid index number.")
        return contact_list

    contact_list.pop(index)
    return contact_list
