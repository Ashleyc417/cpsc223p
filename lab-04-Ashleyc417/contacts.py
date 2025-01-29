# Name: Ashley Chan
# Date: 09/27/2023
# Purpose of File: Contacts Module

'''
This function will add a contact to the contact dictionary.
'''
def add_contact(contacts, id, first_name, last_name):
    if id in contacts:
        return 'error'
    else:
        contacts[id] = [first_name, last_name]
        return contacts[id]
    
'''
This function will modify a contact in the contact dictionary.
'''
def modify_contact(contacts, id, first_name, last_name):
    if id not in contacts:
        return 'error'
    else: 
       contacts[id] = [first_name, last_name] 

'''
This function will delete a contact in the contact dictionary.
'''
def delete_contact(contacts, id):
    if id not in contacts:
        return 'error'
    else: 
       return contacts.pop(id) 
    
'''
This function will sort the contact dictionary in ascending order 
by last name, then by first name.
'''
def sort_contacts(contacts):
    return contacts

'''
This function will find a contact in the contact dictionary.
'''
def find_contact(contacts, find):
    new_dict = dict()
    if find.isnumeric():
        i = int(find)
        if i in contacts:
            new_dict[i] = contacts[i]
        return new_dict
    
    else:
        # Make find lowercase
        find = find.lower()
        for key, value in contacts.items():
            if find == value[0].lower() or find == value[1].lower():
                new_dict[key] = value
        return new_dict