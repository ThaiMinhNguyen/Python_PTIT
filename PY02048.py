n, k = map(int, input().split())
a = list(set(list(map(int, input().split()))))
a.sort()
res = []
b = []
b.append(a[0])
for i in range(1,len(a)):
    if a[i] - a[i-1] > k:
        res.append(b)
        b = []
        b.append(a[i])
    else:
        b.append(a[i])
if len(b):
    res.append(b)
# print(res)
print(len(res))