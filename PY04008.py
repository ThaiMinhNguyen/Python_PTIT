
t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    # a, b = [[0] * m] * n, []
    a = []
    b = []
    y = []
    idx = 0
    for i in range(n):
        y.extend(list(map(int, input().split())))
    for i in range(n):
        x = []
        for j in range(m):
            x.append(y[idx])
            idx+=1
        a.append(x)
    # print(a)
    for i in range(m):
        x = []
        for j in range(n):
            x.append(a[j][i])
        b.append(x)

    for i in range(n):
        for j in range(n):
            s = 0
            for z in range(m):
                s += a[i][z] * b[z][j]
            print(s, end=' ')
        print()