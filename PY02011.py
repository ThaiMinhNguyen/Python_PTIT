n = int(input())
a = list(map(int, input().split()))
k = 0
res = 2**20
for i in range(n):
    s = 0
    crt = a[i]
    for j in range(n):
        s += abs(a[i] - a[j])
    if(res > s):
        res = s
        k = a[i]
print(res, k)

