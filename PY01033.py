
import math
def check(n, m):
    y = math.gcd(int(n), int(m))
    if (y == 1):
        return True
    else:
        return False

a, b = map(int,input().split())
for i in range(a, b+1):
    for j in range(i+1, b+1):
        for l in range(j+1, b+1):
            if check(i, j) and check(i, l) and check(j, l):
                print('(' + str(i) + ', ' + str(j) + ', ' +  str(l) + ')')
