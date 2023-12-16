for _ in range(int(input())):
    a, b = map(int, input().split())
    ls = [int(i) for i in input().split()]
    m = max(ls)
    am = []
    duong = []
    c = 0
    for i in ls:
        if i < 0:
            if i == m and c == 0:
                c = 1
                am.append(b)
            am.append(i)
        if i >= 0:
            if i == m and c == 0:
                c = 1
                duong.append(b)
            duong.append(i)
    for i in am:
        print(i , end=" ")
    for i in duong:
        print(i, end=" ")
    print()
