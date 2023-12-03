import math

def check(n):
    s = str(n)
    return s == s[::-1]

n, m = map(int , input().split())
a = []
for _ in range(n):
    a.append(list(map(int, input().split())))
mn = 0
for i in a:
    for j in i:
        if check(j) and j > 10:
            mn = max(mn, j)
if mn == 0:
    print("NOT FOUND")
else:
    print(mn)
    for i in range(n):
        for j in range(m):
            # print(a[i][j])
            if mn == a[i][j]:
                print('Vi tri [', i, '][', j, ']', sep='')