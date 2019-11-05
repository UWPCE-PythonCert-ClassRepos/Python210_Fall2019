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
    print("\nDictionary Lab 01")
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

    print("\nDictionary Lab 02")

    chris_dict = {
        'Name': 'Chris',
        'City': 'Seattle',
        'Cake': 'Chocolate'
    }

    chris_dict_counted = {}

    for k, v in chris_dict.items():
        chris_dict_counted[k] = v.lower().count('t')

    print(chris_dict_counted)


def set_lab_01():
    """

    Create sets s2, s3 and s4 that contain numbers from zero through twenty, divisible by 2, 3 and 4 (figure out a way to compute those – don’t just type them in).
    Display the sets.
    Display if s3 is a subset of s2 (False)
    and if s4 is a subset of s2 (True).
    """

    print("\nSet Lab 01")

    def create_set(n):
        """
        Return a set of multiples of n that are in range 1-20 inclusive.
        """
        multiples = set()
        for i in range(1, 21):
            if i % n == 0:
                multiples.add(i)
        return multiples

    s2 = create_set(2)
    s3 = create_set(3)
    s4 = create_set(4)

    print('s2: ', s2)
    print('s3:', s3)
    print('s4', s4)
    print('Is s3 a subset of s2? ', s3.issubset(s2))
    print('Is s4 a subset of s2? ', s4.issubset(s2))


def set_lab_02():
    """
    Create a set with the letters in ‘Python’ and add ‘i’ to the set.
    Create a frozenset with the letters in ‘marathon’.
    Display the union and intersection of the two sets.
    """
    print("\nSet Lab 02")
    python = set()
    for i in 'Python':
        python.add(i)

    print(python)

    python.add('i')

    marathon = set()
    for i in 'marathon':
        marathon.add(i)

    frozen_marathon = frozenset(marathon)

    print(frozen_marathon)

    print('Union: ', python | frozen_marathon)
    print ('Intersection: ', python & frozen_marathon)


if __name__ == '__main__':
    dict_lab_01()
    dict_lab_02()
    set_lab_01()
    set_lab_02()
