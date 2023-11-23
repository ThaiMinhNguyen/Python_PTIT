import math

def check(n):
    for i in range (2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return n > 1

n, m = map(int , input().split())
a = []
for _ in range(n):
    a.append(list(map(int, input().split())))
mn = 0
for i in a:
    for j in i:
        if check(j):
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