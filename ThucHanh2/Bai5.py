import math
from sys import setrecursionlimit

setrecursionlimit(100000)

x = 3 + math.sqrt(5)
def pow(n):
    if n == 0: return 1
    tmp = pow(n//2)
    if n % 2 == 1: return (tmp*tmp*x)
    return tmp*tmp

for t in range(int(input())):
    n = int(input())
    sum = int(pow(n)%1000)
    print(f"Case #{t+1}: {sum:03d}")