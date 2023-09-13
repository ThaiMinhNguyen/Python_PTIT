import math

def check(n):
    for i in range (2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return n > 1

for t in range(int(input())):
    a = int(input())
    k = 0
    for i in range(1, a):
        if math.gcd(i, a) == 1:
            k = k+1

    if check(k):
        print("YES")
    else:
        print("NO")
