
def series1(fruit_list):
    # Ask the user for another fruit and add it to the end of the list.
    # Display the list.
    print("SERIES 1======")
    response = input("What fruit would you like to add?000 ")
    fruit_list.append(response)
    print(fruit_list)


    # Ask the user for a number and display the number back to the user and the fruit corresponding to
    # that number (on a 1-is-first basis). Remember that Python uses zero-based indexing, so you will need to correct
    response = input("Pick a fruit from the list?")

    print("index number: " + response)
    print("Fruit: " + fruit_list[int(response)])

    # Add another fruit to the beginning of the list using “+” and display the list.
    print("Adding Banana to end of list")
    fruit_list = (fruit_list + ["Banana"])
    print(fruit_list)

    # Add another fruit to the beginning of the list using insert() and display the list.
    print("Inserting Pineapple in beginning of list")
    fruit_list.insert(0, "Pineapple")

    # Display all the fruits that begin with “P”, using a for loop.
    for fruit in fruit_list:
        if "P" == fruit[0]:
            print(fruit)


def series2(fruit_list):
    # Display the list.
    # Remove the last fruit from the list.
    print("SERIES 2======")
    print(fruit_list)
    fruit_list.pop(len(fruit_list) - 1)
    print("Removed last fruit from list")
    print(fruit_list)

    # Ask the user for a fruit to delete, find it and delete it.
    # (Bonus: Multiply the list times two. Keep asking until a match is found. Once found, delete all occurrences.)

    fruit_list_2 = fruit_list * 2
    print(fruit_list_2)
    response = input("Which fruit do you want to delete")

    if response in fruit_list_2:
        for fruit in fruit_list_2:
            if response == fruit:
                fruit_list_2.remove(fruit)
    else:
        print("Fruit not in list")

    print(fruit_list_2)


def series3(fruit_list):
    # Ask the user for input displaying a line like “Do you like apples?” for each fruit in the list (making the fruit all lowercase).
    # For each “no”, delete that fruit from the list.
    # For any answer that is not “yes” or “no”, prompt the user to answer with one of those two values (a while loop is good here)
    # Display the list.

    print("SERIES 3======")
    fruit_count = len(fruit_list)
    list_count = 0

    while list_count < fruit_count:

        response = input("Do you like " + fruit_list[list_count].lower() +"?")

        ## Yes increases the index, and No decreases the total fruit count
        if response == 'yes':
            list_count += 1
        elif response == 'no':
            fruit_list.remove(fruit_list[list_count])
            fruit_count -= 1
        else:
            print('Please answer with a "yes" or "no". ')


    print(fruit_list)


def series4(fruit_list):
    # Make a new list with the contents of the original, but with all the letters in each item reversed.
    # Delete the last item of the original list. Display the original list and the copy.
    new_list = []

    for fruit in fruit_list:
        new_list.append(fruit[::-1])

    new_list.pop(-1)

    print("SERIES 4======")
    print(fruit_list)
    print(new_list)

if __name__ == "__main__":
    fruit_list = ["Apples", "Pears", "Oranges", "Peaches"]
    series1(fruit_list)
    series2(fruit_list)
    series3(fruit_list)
    series4(fruit_list)


