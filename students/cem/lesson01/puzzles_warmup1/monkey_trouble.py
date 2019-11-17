"""
monkey_trouble @ https://codingbat.com/prob/p120546
We have two monkeys, a and b, and the parameters a_smile and b_smile indicate if each is smiling.
We are in trouble if they are both smiling or if neither of them is smiling. Return True if we are in trouble.
"""


def monkey_trouble(a_smile, b_smile):
    if a_smile and b_smile:
        return True
    if not a_smile and not b_smile:
        return True
    else:
        return False


both_smiling_monkeys = monkey_trouble(a_smile=True, b_smile=True)
neither_smiling_monkeys = monkey_trouble(a_smile=False, b_smile=False)
monkey_a_smiling_alone = monkey_trouble(a_smile=True, b_smile=False)
monkey_b_smiling_alone = monkey_trouble(a_smile=False, b_smile=True)

print("Both monkeys are smiling, Are we in trouble?", both_smiling_monkeys)
print("Neither monkeys are smiling, Are we in trouble?", neither_smiling_monkeys)
print("Monkey A is smiling but not Monkey B, Are we in trouble?", monkey_a_smiling_alone)
print("Monkey A is not smiling but Monkey B is smiling, Are we in trouble?", monkey_b_smiling_alone)
