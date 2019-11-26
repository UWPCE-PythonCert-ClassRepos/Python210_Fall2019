# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 08:22:00 2019

@author: Ken.Clark
"""

contact = {'name': 'chris', 'city': 'Seattle', 'cake': 'strawberry'}


def menu_dict():
    while True:
        """
        Menu: 
        """
        usr_input = input("Please select an action:\n"
                            "1. Add fruit\n"
                            "2. Delete last item\n"
                            "3. Display keys\n"
                            "4. check for cake\n"
                            "5. check for mango\n"
                            "6. To exit\n"
                            ">>>")
        menu_dict= {
                '1': add_fruit, '2': delete_last,
                '3': display_keys, '4': check_for_cake,
                '5': check_for_mango, '6': sys.exit,
                }
        selection = menu_dict[usr_input]
        try:
            selection()
        except TypeError:
            print(selection)



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
    menu_dict()