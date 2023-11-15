a = [0]*25
res = []
lst = []
n, k = [int(x) for x in input().split()]
lst = list(map(str, input().split()))
lst.sort()
for i in lst:
    if i not in res:
        res.append(i)
n = len(res)

def sinh(i):
    for j in range(a[i-1]+1, n-k + i+1):
        a[i] = j
        if i == k:
            for l in range(1, k+1):
                print(res[a[l] - 1], end=" ")
            print()
        else:
            sinh(i+1)

sinh(1)

