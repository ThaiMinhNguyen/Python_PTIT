res = []
for _ in range(int(input())):
    res.append([input(), input(), input()])
res.sort(key=lambda x: x[0])
for i in res:
    print(*i)