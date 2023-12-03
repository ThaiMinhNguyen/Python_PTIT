n = int(input())
l = {}
for _ in range(n-1):
    a, b = map(int, input().split())
    if a not in l:
        l[a] = [b]
    else:
        l[a].append(b)
    if b not in l:
        l[b] = [a]
    else:
        l[b].append(a)
c = 0
# for k, v in l.items():
#     print(k, v)
for k, v in l.items():
    if c == 0:
        if len(v) == n-1:
            c = 1
    else:
        if len(v) != 1:
            c = 0
            break
if c == 1:
    print("Yes")
else:
    print("No")

