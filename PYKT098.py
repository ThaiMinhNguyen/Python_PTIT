f = open("DATA.in", "r")
res = []
m = 0
for i in f:
    k = i.split()
    for i in k:
        if not i.isdigit() or int(i) > 2147483647 or int(i) < -2147483648:
            res.append(i)
res.sort()
print(*res)