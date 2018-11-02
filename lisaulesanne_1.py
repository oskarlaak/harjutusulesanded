with open('numbrid.txt', 'r') as myfile:
    total = 0
    for line in myfile:
        for char in line:
            total += int(char)
    print(total)
