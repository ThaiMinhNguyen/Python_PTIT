import math

def check(n):
    for i in range (2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return n > 1

input()
a = list(map(int, input().split()))
b = []
for i in a:
    if check(i):
        b.append(i)
b.sort()
j = 0
for i in range(len(a)):
    if check(a[i]):
        a[i] = b[j]
        j+=1
print(*a)