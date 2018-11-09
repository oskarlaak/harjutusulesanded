from random import randint

# getting words from text file into list
words = []
with open('words.txt', 'r') as myfile:
    for line in myfile:
        words.append(line.replace('\n', ''))


# replacing not picked characters with '_'
def update():
    word = list(random_word)
    for c, char in enumerate(random_word):
        if char not in picked_chars:
            word[c] = '_'
    return ''.join(word)


# creating variables
random_word = words[randint(0, len(words) - 1)]
picked_chars = []
lives = 5
output = update()

# main loop
print('Welcome to the game!')
end = False
while not end:
    print(' '.join(output))
    user_input = input('guess a letter: ')
    if len(user_input) == 1 and user_input not in picked_chars:
        picked_chars.append(user_input)
        if user_input not in random_word:
            lives -= 1
    else:
        lives -= 1

    output = update()
    if output == random_word:
        print(' '.join(output))
        print('Word solved. You won!')
        end = True
    elif lives == 0:
        print('Lives lost. You lose!')
        print('The word was:', ' '.join(random_word))
        end = True
    else:
        print('picked chars =', sorted(picked_chars))
        print('lives =', lives)
