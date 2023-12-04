f = open("VANBAN.in", "r")
res = {}
m = 0
for i in f:
    k = i.split()
    for i in k:
        if i == i[::-1]:
            if i not in res:
                res[i] = 1
                m = max(m, len(i))
            else:
                res[i] += 1

for k, v in res.items():
    if len(k) == m:
        print(k, v)
