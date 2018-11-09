def reverse(s):
    s = list(s)
    reversed_s = []
    for i in range(len(s) - 1, -1, -1):
        reversed_s.append(s[i])
    return ''.join(reversed_s)
