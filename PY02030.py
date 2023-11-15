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
    if i not in b:
        b.append(i)
# print(*b)
l = 0
r = sum(b)
res = -1
for i in range(0,len(b)):
    l += b[i]
    r -= b[i]
    # print(l, r)
    # print(b[i])
    if check(l) and check(r):
        res = i
        break
if res == -1:
    print("NOT FOUND")
else:
    print(res)