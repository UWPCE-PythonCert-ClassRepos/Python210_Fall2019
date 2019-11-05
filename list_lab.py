#James Spaulding
#Thank You Both for the extension
#I was called into work Friday so I am submitting this Thursday late, I cant see extending the work further.
#Thank you both

# Series 1
fruitList1 = ["Apples", "Pears", "Oranges", "Peaches"]
print(fruitList1)

#Ask the user for another fruit and add it to the end of the list and print it.
newFruit = input('Enter a Fruit: ')
fruitList1.append(newFruit)
print(fruitList1)

#Ask the user for a number and display the number

numFruit = int(input('Enter a Number: '))
print(numFruit)
print(fruitList1[numFruit -1])

#Add another fruit and display

newFruit2 = input('Enter a new Fruit: ')
print(newFruit2)
print(fruitList1)
fruitList1 = [newFruit2] + fruitList1
print(fruitList1)

#Add another fruit to the beginning of the list using insert() and display the list.
newFruit3 = input('Enter a new Fruit: ')
fruitList1.insert(0, newFruit3)
print(fruitList1)

#Display all the fruits that begin with “P”, using a for loop.
newlist1 = []
for i in fruitList1:
    if i.startswith('P'):
        newlist1.append(i)
print(newlist1)
#Series 2

#Using the list created in series 1 above:

    #Display the list.
print(fruitList1)
    #Remove the last fruit from the list.
del fruitList1[-1]
    #Display the list.
print(fruitList1)
    #Ask the user for a fruit to delete, find it and delete it.
newFruit4 = input('Enter fruit from list above to delete: ')
if fruitList1.__contains__(newFruit4):
    fruitList1.remove(newFruit4)
print('missed your chance to remove one buddy!')
print(fruitList1)




#Series 3

List = fruitList1
List = [item.lower() for item in List]
print(List)

# Ask the user for input displaying a line like “Do you like apples?”
# For each “no”, delete that fruit from the list.
# For any answer that is not “yes” or “no”,prompt the user to
# answer with one of those two values (a while loop is good here)

keepit = []
tossit = []
number=len(List[:])
for i in range(number):
    fruit = str(input(('Do you like  ' + List[i] + '? '))).upper().strip()
    print(fruit)
    if fruit != 'Y' and fruit !='N':
        while fruit != 'Y' and fruit != 'N':
            fruit = str(input("DO YOU LIKE THE FRUIT Y OR N?")).upper().strip()
            if fruit == 'Y':
                print('excellent')
            if fruit == 'N':
                print('hmm')
    if fruit == 'Y':
        print('excellent')
        keepit.append(List[i])
    else:
        tossit.append(List[i])
List=keepit
print(List)
#Series 4

#Once more, using the list from series 1:
fruitList1

    #Make a new list with the contents of the original, but with all the
        #letters in each item reversed.

newlist = [x[::-1] for x in fruitList1][::]
print(newlist)

    #Delete the last item of the original list. Display the original list and the copy.

fruitList1.pop()
print(fruitList1)
print(newlist)

