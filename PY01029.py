import math

for t in range(int(input())):
    x = input()
    y = math.gcd(int(x), int(x[::-1]))
    if(y == 1):
        print("YES")
    else:
        print("NO")
