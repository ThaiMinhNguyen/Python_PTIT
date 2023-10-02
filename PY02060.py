import math

mod = 1000000007


for _ in range(int(input())):
    res = 0
    a, b = map(int, input().split())
    sum = 1
    for i in range(a, b+1):
        sum *= i
        sum = sum % mod
    c = set()
    for i in range(1, int(math.sqrt(sum))+1):
        if(sum % i == 0):
            c.add(i)
            c.add(sum//i)
    c = sorted(c)
    for i in range(len(c)):
        for k in range(i + 1, len(c)):
            if math.lcm(c[i], c[k]) == sum:
                res += 1
                res = res % mod
    res = (res * 2) % mod
    res = (res + 1) % mod
    print(res)