for _ in range(int(input())):
    x = input();
    sum = 0;
    k = []
    for i in x:
        if(i.isdigit()):
            sum += int(i)
        else:
            k.append(i)
    k.sort()
    for i in k:
        print(i, sep="", end="")
    print(sum)