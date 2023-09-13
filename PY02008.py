import math
def isPrime(n):
    for i in range(2, int(math.sqrt(int(n)))+1):
        if n % i == 0:
            return False
    return n > 1


n, x = map(int, input().split())
a = []
i = 2;
while len(a) < n:
    if isPrime(i):
        a.append(i)
    i += 1
print(x, end = " ")
for j in a:
    x += j
    print(x, end = " ")


