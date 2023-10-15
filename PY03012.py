l = []
for _ in range(int(input())):
    s = []
    ten = input()
    a, b = map(int, input().split())
    s.append(ten)
    s.append(a)
    s.append(b)
    l.append(s)

l = sorted(sorted(sorted(l,key=lambda x: x[0]),key= lambda x: x[2]),key= lambda x: x[1],reverse=True)
# l = sorted(l, key= lambda x : (x[1], -x[2], x[0]))
for i in l:
    print(i[0], i[1], i[2])