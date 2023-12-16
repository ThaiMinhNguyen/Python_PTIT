for _ in range(int(input())):
    x = input().split()
    c = 0
    for i in x:
        if c + len(i) > 100:
            break
        else:
            c += len(i) + 1
            print(i, end=' ')
    print()
