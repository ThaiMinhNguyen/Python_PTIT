n = int(input())
a = []
while True:
    a.extend(list(map(int, input().split())))
    if len(a) == n:
        break
chan = []
le = []
for i in a:
    if i % 2 == 0:
        chan.append(i)
    else:
        le.append(i)
chan.sort()
le.sort(reverse=True)
i, j = 0, 0
for k in a:
    if k % 2 == 0:
        print(chan[i], end= " ")
        i+=1
    else:
        print(le[j], end= " ")
        j+=1


