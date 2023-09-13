for t in range(int(input())):
    x = input()
    for i in range(0, 1000):
        if(int(x) % 7 == 0):
            break
        x = str(int(x) + int(x[::-1]))

    if int(x) % 7 == 0:
        print(x)
    else:
        print("-1")