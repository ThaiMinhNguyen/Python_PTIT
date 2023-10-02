for _ in range(int(input())):
    n, m = map(int, input().split())
    x = []
    h = []
    for i in range(n):
        x.append(list(map(int, input().split())))
    for i in range(3):
        h.append(list(map(int, input().split())))
    res = []
    sum = 0
    for i in range(n - 2):
        for j in range(m - 2):
            for k in range(i, i + 3):
                for l in range(j, j + 3):
                    sum += x[k][l] * h[k - i][l - j]
    print(sum)