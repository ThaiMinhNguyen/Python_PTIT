input()
a = list(map(int, input().split()))
b = {}
for i in a:
    if i not in b.keys():
        b[i] = 1
    else:
        b[i] += 1
c = sorted(set(b.values()), reverse=True)
if len(c) == 1:
    print("NONE")
else:
    for k, v in sorted(b.items(), key=lambda x:x[1], reverse=True):
        if v == c[1]:
            print(k)
            break
