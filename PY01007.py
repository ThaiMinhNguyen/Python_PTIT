import math

for t in range(int(input())):
    x, y, z = map(float, input().split())
    k = 0
    while(x < z):
       x = x * (1 + y/100)
       k = k + 1
    print(math.ceil(k))