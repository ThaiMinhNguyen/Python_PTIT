import math

n = int(input())
l = int(n ** (0.5))
a = [i for i in range(l+1)]
res = 0
i = 2
while i * i <= l:
    if a[i] == i:
        for j in range(i*i, l+1, i):
            if a[j] == j:
                a[j] = i
    i+=1
for i in range(2, l+1):
    q = a[i]
    p = a[i // a[i]]
    if p * q == i and p != 1 and p != q:
        res+=1
    elif a[i] == i:
        if pow(i, 8) <= n:
            res+=1
print(res)

# ?????