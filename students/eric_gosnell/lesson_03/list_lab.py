"""**************************************
# Author: Eric Gosnell
# Lesson: 3
# Assignment: List lab exercise
**************************************
"""

# List object used in all series in this exercise.
fruit_list = ["apples", "pears", "oranges", "peaches"]  # Starter values.


def series_one():
    global fruit_list   # Reference global list from within function

    print("Fruit list:", fruit_list)

    response = input("\nPlease add another fruit for the list. >")
    fruit_list.append(response.lower())

    response = int(input("\nPlease enter a number between {} and {}. >".format(1, len(fruit_list))))
    print("Fruit list item #", response, "is", fruit_list[response - 1])

    response = input("\nPlease add another fruit for the list. >")
    fruit_list = [response.lower()] + fruit_list
    print("New fruit list:", fruit_list)

    response = input("\nPlease add another fruit for the list. >")
    fruit_list.insert(0, response.lower())
    print("New fruit list:", fruit_list)

    print("\nFruit list items starting with P:")
    for fruit in fruit_list:
        if fruit[0] == "p":
            print(fruit)
        else:
            pass


def series_two():
    global fruit_list

    print("\n********     Series Two     ********")
    print("\nSeries two starting fruit list:", fruit_list)
    fruit_list.pop()
    print("\nFruit list with last item removed:", fruit_list)

    response = input("\nPlease enter the name of a fruit to delete from the list. >")
    for fruit in fruit_list[:]:
        if response.lower() == fruit.lower():
            fruit_list.remove(fruit)
        else:
            pass
    print("\nNew fruit list:", fruit_list)

    # Bonus task in series 2
    print("\n*** Bonus Task ***")

    fruit_list += fruit_list

    done = None
    while not done:     # While loop used to repeatedly prompt user to enter another fruit.
        print("\nFruit list doubled!\n")
        print(fruit_list)
        response = input("\nPlease enter the name of another fruit to delete from the list. >")

        counter = 0
        for fruit in fruit_list[:]:
            if response.lower() == fruit.lower():
                fruit_list.remove(fruit)
                counter += 1
            else:
                pass

        if counter:
            print()
            print(response.lower(), "found", counter, "times and removed.  Updated list:\n")
            print(fruit_list)
            done = True
        else:
            print()
            print(response.lower(), "not found in list!")
            fruit_list += fruit_list


def series_three():
    global fruit_list

    # Add additional fruit to list to grow it, to work with loops to delete multiple copies of elements.
    fruit_list.append("bananas")
    fruit_list.append("strawberries")
    fruit_list.append("apples")


    print("\n********     Series Three     ********")
    print("\nSeries three starting fruit list:")
    print(fruit_list, "\n")

    answer_list = []        # Answer list so that user is not prompted multiple times about same fruit name.
    for copy in fruit_list[:]:
        answer_list.append(copy)
        if answer_list.count(copy) < 2:
            response = input("Do you like " + str(copy) + "? Answer 'yes' or 'no'? >")
            while response != 'yes' and response != "no":
                response = input("Invalid input!  Answer 'yes or 'no'. >")
            if response == "no":
                for fruit in fruit_list:
                    if fruit == copy:
                        fruit_list.remove(fruit)
                    else:
                        pass
            else:
                pass
        else:
            pass


    print("\nUpdated list:")
    print(fruit_list)


def series_four():
    global fruit_list

    print("\n********     Series Four     ********")
    print("\nSeries four starting fruit list:")
    print(fruit_list, "\n")

    copy_list = fruit_list[:]

    for i in range(len(fruit_list)):
        copy_list[i] = fruit_list[i][::-1]

    fruit_list.pop()

    print("Copy_list: ", copy_list)
    print("Updated original fruit_list: ", fruit_list)


if __name__ == "__main__":
    series_one()
    series_two()
    series_three()
    series_four()

