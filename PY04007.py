# import numpy as np

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    a, b = [[0] * m] * n, []
    for i in range(n):
        a[i] = [int(x) for x in input().split()]
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


    # k1 = np.array(a)
    # k2 = np.array(b)
    # res = k1.dot(k2)
    # for i in range(n):
    #     for j in range(n):
    #         print(res[i][j], end= " ")
    #     print()
# 1
# 2  2
# 1  2
# 3  4