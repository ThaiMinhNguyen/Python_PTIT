m, n  = map(int, input().split())
a = [] * m
for i in range(m):
    ls = list(map(int, input().split()))
    a.append(ls)
for i in range(m):
    for j in range(n):
        if a[i][j] = -1:
            if i == 0 and j == 0:
                a[i][j + 1] = -2 if a[i][j + 1] != -1
                a[i + 1][j + 1] = -2 if a[i + 1][j + 1] != -1
                a[i + 1][j] = -2 if a[i + 1][j] != -1
            elif i == 0 and j == n-1:
                a[i][j - 1] = -2 if a[i][j - 1] != -1
                a[i + 1][j - 1] = -2 if a[i + 1][j - 1] != -1
                a[i + 1][j] = -2 if a[i + 1][j] != -1
            elif i == m-1 and j == n-1:
                a[i][j - 1] = -2 if a[i][j - 1] != -1
                a[i - 1][j - 1] = -2 if a[i - 1][j - 1] != -1
                a[i - 1][j] = -2 if a[i - 1][j] != -1
            elif i == m-1 and j == 0:
                a[i-1][j] = -2 if a[i-1][j] != -1
                a[i - 1][j + 1] = -2 if a[i - 1][j + 1] != -1
                a[i][j + 1] = -2 if a[i][j + 1] != -1
            elif i == 0:
                a[i][j - 1] = -2 if a[i][j-1] != -1
                a[i][j + 1] = -2 if a[i][j + 1] != -1
                a[i + 1][j + 1] = -2 if a[i + 1][j + 1] != -1
                a[i + 1][j - 1] = -2 if a[i + 1][j - 1]!= -1
                a[i+1][j] = -2 if a[i+1][j] != -1
            elif j == 0:
                a[i - 1][j] = -2 if a[i][j - 1] != -1
                a[i + 1][j] = -2 if a[i][j + 1] != -1
                a[i + 1][j - 1] = -2 if a[i + 1][j + 1] != -1
                a[i - 1][j - 1] = -2 if a[i + 1][j - 1] != -1
                a[i + 1][j] = -2 if a[i + 1][j] != -1

print(*a)