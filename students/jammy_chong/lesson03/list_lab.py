def create_list():
    global fruit_list
    fruit_list = ["Apples", "Pears", "Oranges", "Peaches"]

#Seris 1
create_list()
print(fruit_list)

new_fruit = input("Add another fruit to the end of the list: ")
fruit_list.append(new_fruit)
print(fruit_list)

user_number = input(f"Choose a number from 1 to {len(fruit_list)} to display fruit: ")
print(f"The fruit you chose is {fruit_list[int(user_number)-1]}")

second_fruit = input("Add another fruit to the beginning of the list: ")
fruit_list = [second_fruit] + fruit_list
print(fruit_list)

third_fruit = input("Add another fruit to the beginning of the list: ")
fruit_list.insert(0, third_fruit)
print(fruit_list)

print("The fruits that start with P are: " )
for fruit in fruit_list:
    if fruit[0] == "P":
        print(fruit)

#Series 2
create_list()

fruit_list.pop()
print(fruit_list)

#Bonus
fruit_list = fruit_list * 2
print(fruit_list)

#confirm_delete = 1
while True:
    delete_fruit = input("Type the fruit you want to delete :")
    if delete_fruit in fruit_list:
        for x in range(fruit_list.count(delete_fruit)):
            fruit_list.remove(delete_fruit)
        break
        #confirm_delete = 0

print(fruit_list)

#Series 3
create_list()
print(fruit_list)
fruits_to_delete = []

for fruit in fruit_list:
    like = input(f"Do you like {fruit}?: ")
    while like not in("yes","no"):
        like = input("Please enter yes or no: ")
    if like == "no":
        fruits_to_delete.append(fruit)

for fruit in fruits_to_delete:
    fruit_list.remove(fruit)

if len(fruit_list) > 1:
    print(f"You like these fruits: {fruit_list}.")
elif len(fruit_list) == 1:
    print(f"You like this fruit: {fruit_list[0]}.")
else:
    print("You don't like any fruit from the list.")

#Series 4
create_list()
new_list = []

for item in fruit_list:
    new_list.append(item[::-1])

fruit_list.pop()
print(f"Original list: {fruit_list}. New List: {new_list}.")
