
import math
def check(n, m):
    y = math.gcd(int(n), int(m))
    if (y == 1):
        return True
    else:
        return False

x, z = map(int,input().split())
s = 0
for i in range(10**(z-1), 10**z-1):
    if check(x, i):
        if s < 9:
            s = s + 1
            print(i, end = ' ')
        else:
            s = 0
            print(i)