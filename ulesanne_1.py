def remove_numbers(s):
    removables = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, ' ']
    for char in removables:
        s = s.replace(str(char), '')
    return s

def lowercase(s):
    return s.lower()

def uppercase_first(s):
    return s.title()

name = input('Sisestage suvaline nimi:\n')
name = uppercase_first(remove_numbers(name))

adjective = input('Sisestage suvaline omadussõna:\n')
adjective = lowercase(remove_numbers(adjective))

noun = input('Sisestage suvaline nimisõna:\n')
noun = lowercase(remove_numbers(noun))

verb = input('Sisestage suvaline tegusõna:\n')
verb = lowercase(remove_numbers(verb))

print('Mina, {0}, olen {1} {2} ja ma {3}'.format(name, adjective, noun, verb))