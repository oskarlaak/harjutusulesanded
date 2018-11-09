import string
alphabet = list(string.ascii_lowercase)

#not very readable
def ceasar_cipher(s):
    s = list(s.lower())
    for c1, char1 in enumerate(s):
        for c2, char2 in enumerate(alphabet):
            if char2 == char1:
                pos = c2
                break
        
        if pos == len(alphabet) - 1:
            s[c1] = 'a'
        else:
            s[c1] = alphabet[pos + 1]
    return ''.join(s)
