# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 08:22:00 2019

@author: Ken.Clark
"""

contact = {'name': 'chris', 'city': 'Seattle', 'cake': 'strawberry'}


def menu():
    """
    Menu: Could not get to work won't pass user choice in correct 
    form
    """
    usr_input = input("Please select an action:\n"
                        "1. Add fruit\n"
                        "2. Delete last item\n"
                        "3. Display keys\n"
                        "4. check for cake\n"
                        "5. check for mango\n"
                        "6. To exit\n"
                        ">>>")
    menu_dict = {
            '1': 'add_fruit', '2': 'delete_last_item()',
            '3': 'display_keys()', '4': 'check_for_cake()',
            '5': 'check_for_mango()', '6': 'exit()'
            }

    selection = usr_input.strip().lower()
    action = [menu_dict.get(selection, None)]
    action()


def delete_last():
    """Delete last item using pop"""
    contact.popitem()
    print("Removed last item:\n  ", contact)


def add_fruit():
    """Add friut and mango to the dictionary"""
    a = {'friut': 'mango'}
    contact.update(a)
    print("Add friut and mango:\n  ", contact)


def display_keys():
    """Display dictionary keys"""
    print("Dispay keys:\n  ", contact.keys())


def check_for_cake():
    """Check for cake in dictionary key"""
    "cake" in contact
    if True:
        print("There is cake: Return True")
    else:
        print("No cake here")


def check_for_mango():
    """Check for mango in dictionary values"""
    "mango" in contact.values()
    if True:
        print("There is mango: Return True")
    else:
        print("No cake here")


def main():
    add_fruit()
    display_keys()
    check_for_cake()
    check_for_mango()
    delete_last()


if __name__ == "__main__":
    #menu()
    main()