DNA_chars = ['a', 'c', 'g', 't']

def is_DNA(s):
    s = list(s.lower())
    for char in s:
        if char not in DNA_chars:
            return False
    return True
