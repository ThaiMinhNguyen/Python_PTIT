for t in range(int(input())):
    x = input()
    temp = 0
    c = x[0]
    for i in x:
        if i == c:
            temp = temp + 1
        else:
            print(temp, c, sep='', end = '')
            temp = 1
            c = i
    print(temp, c, sep = '')
    # print()

