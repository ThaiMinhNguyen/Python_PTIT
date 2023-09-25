import math
def isPrime(n):
    for i in range(2, int(math.sqrt(int(n)))+1):
        if n % i == 0:
            return False
    return n > 1

n = int(input())
a = list(map(int, input().split()))
b = []
for i in a:
    if i not in b:
        b.append(i)
# print(b)
for i in (b):
    if(isPrime(i)):
        print(i, a.count(i))
