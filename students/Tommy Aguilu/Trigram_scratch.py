import random

words = {('I', 'wish'): ['I', 'I'], ('wish', 'I'): ['may', 'might'], ('I', 'may'): ['I'], ('may', 'I'): ['wish']}
def build_new(trigrams):
    output_list = []
    for pair in trigrams:
        output_list.append(pair)
    working_pair = output_list[0]
    text = [working_pair[0],working_pair[1]]
    for i in range(len(trigrams)):
        if working_pair in trigrams:
            text.append(random.choice(trigrams[working_pair]))
            working_pair = (text[-2],text[-1])

    return " ".join(text)

print(build_new(words))