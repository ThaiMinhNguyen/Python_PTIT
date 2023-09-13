for t in range(int(input())):
    x = input()
    for i in x:
        if i.isalpha():
            temp = i
        else:
            for j in range(int(i)):
                print(temp, end = '')
    print()