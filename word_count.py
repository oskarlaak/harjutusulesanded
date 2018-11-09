def word_count(s):
    words = s.split()
    dictionary = {}
    for word in words:
        if word not in dictionary:
            dictionary[word] = 1
        else:
            dictionary[word] += 1
    return dictionary
