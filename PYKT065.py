import math

def check(n):
    for i in range (2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return n > 1

ls = []
for i in range(2, 48):
    if check(i):
        ls.append(i)
while(True):
    x = input()
    if(x == '-1'):
        break
    res = 0
    a, b = map(int, x.split())
    n = int(input())
    for i in range(a, b+1):
        c = 1
        for j in ls:
            if i % j == 0:
                c = 0
                break
        if c == 0:
            continue
        else:
            res+=1
    print(res)
# 1 10
# 10
# 2001 2309
# 50
# 34 2003
# 50
# -1
