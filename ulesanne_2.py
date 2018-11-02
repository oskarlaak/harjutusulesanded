from random import randint

words = []
with open('words.txt', 'r') as myfile:
    for line in myfile:
        words.append(line.replace('\n', ''))

random_word = words[randint(0, len(words) - 1)]

picked_chars = []

def update(word):
    for c, char in enumerate(word):
        if char not in picked_chars:
            word[c] = '_'
    return word

print(update(random_word))