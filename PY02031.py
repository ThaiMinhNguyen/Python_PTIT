import math

def isPrime(n):
    if n < 2: return False
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            return False
    return True

n, m = map(int, input().split())
a = []
for i in range(n):
    b = list(map(int, input().split()))
    for i in range(len(b)):
        if isPrime(b[i]):
            b[i] = 1
        else:
            b[i] = 0
    a.append(b)
for i in a:
    for j in i:
        print(j, end = " ")
    print()

# 3 3
# 1 2 3
# 4 5 6
# 7 8 9