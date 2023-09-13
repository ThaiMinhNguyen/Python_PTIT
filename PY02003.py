import math

def isHamming(x):
    s = [2, 3, 5]
    for i in s:
        while x % i == 0:
            x = x/i
    return x == 1

def HammingOrder(x):
    a = [0] * (x+1)
    a[1] = 1
    p2 = p3 = p5 = 1
    for i in range(2, x+1):
        while a[p2]*2 <= a[i-1]:
            p2 = p2 +1
        while a[p3] * 3 <= a[i - 1]:
            p3 = p3 + 1
        while a[p5] * 5 <= a[i - 1]:
            p5 = p5 + 1
        a[i] = min(a[p2]* 2, a[p3]*3, a[p5]*5)
    if isHamming(x):
        return a[x]
    else:
        return "Not in sequence"




for t in range(int(input())):
    x = int(input())
    print(HammingOrder(x))

