from math import gcd
for _ in range(int(input())):
    a, b = map(int, input().split())
    ls = []
    while(True):
        x = list(map(int, input().split()))
        ls += x
        if len(ls) == a:
            break
    res = 1001
    for i in range(0, a):
        g = ls[i]
        for j in range(i, a):
            g = gcd(g, ls[j])
            if g == b:
                res = min(res, j - i +1)
    print(res) if res != 1001 else print(-1)
