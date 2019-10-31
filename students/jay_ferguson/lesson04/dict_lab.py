#!/usr/bin/env python3

def dict_lab_01():
    """

    Create a dictionary containing “name”, “city”, and “cake” for “Chris” from
        “Seattle” who likes “Chocolate” (so the keys should be: “name”, etc, and values: “Chris”, etc.)
    Display the dictionary.
    Delete the entry for “cake”.
    Display the dictionary.
    Add an entry for “fruit” with “Mango” and display the dictionary.
    Display the dictionary keys.
    Display the dictionary values.
    Display whether or not “cake” is a key in the dictionary (i.e. False) (now).
    Display whether or not “Mango” is a value in the dictionary (i.e. True).
    """
    chris_dict = {
        'Name': 'Chris',
        'City': 'Seattle',
        'Cake': 'Chocolate'
    }

    print(chris_dict)

    del (chris_dict['Cake'])

    print(chris_dict)

    for value in chris_dict.values():
        print("Dictionary value: {}".format(value))

    print("'Cake' in the dictionary? {}".format('Cake' in chris_dict.keys()))
    print("'Mango' in the dictionary? {}".format('Mango' in chris_dict.values()))


def dict_lab_02():
    """

    Using the dictionary from item 1: Make a dictionary using the same keys
    but with the number of ‘t’s in each value as the value (consider upper and lower case?).

    The result should look something like:

    {"name": 0
     "city": 2
     "cake": 2
    }
    """

    chris_dict = {
        'Name': 'Chris',
        'City': 'Seattle',
        'Cake': 'Chocolate'
    }

    chris_dict_counted = {}

    for k, v in chris_dict.items():
        chris_dict_counted[k] = v.lower().count('t')

    print(chris_dict_counted)


try:
    while True:
        print("Hello!")
except KeyboardInterrupt:
    print("Phew! We're done.")
