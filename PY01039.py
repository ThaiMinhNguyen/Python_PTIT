for t in range(int(input())):
    x = input()
    y = set(list(x))
    check = 0
    if len(y) == 2:
        for i in range(0, len(x) - 2, 1):
            if(x[i] != x[i+2]):
                print("NO")
                check = 1
                break
        if check == 0:
            print("YES")
    else:
        print("NO")