# Name: Ashley Chan
# Date: 09/13/2023
# Purpose: Contacts Module

def add_contact(contact_list, first_name, last_name):
    contact_list.append([first_name, last_name])

def modify_contact(contact_list, first_name, last_name, index):
    if index in range (len(contact_list)):
        contact_list[index] = [first_name, last_name]
        return True
    else:
        return False
    
def delete_contact(contact_list, index):
    if index in range (len(contact_list)):
        del contact_list[index]
        return True
    else:
        return False

def sort_contacts(contact_list, column):
    if column == 0:
        contact_list.sort(key = lambda x : x[0])
    elif column == 1:
        contact_list.sort(key = lambda x : x[1])
    else: 
        return
