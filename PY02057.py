
n, m = map(int , input().split())
a = []
for _ in range(n):
    a.append(list(map(int, input().split())))
mx = 0
mn = min(a[0])
for i in a:
    mx = max(mx, max(i))
    mn = min(mn, min(i))
x = mx - mn
# print(x)
c = 0
for i in a:
    if x in i:
        c = 1
if c == 1:
    print(x)
    for i in range(n):
        for j in range(m):
            # print(a[i][j])
            if x == a[i][j]:
                print('Vi tri [', i, '][', j, ']', sep='')
else:
    print("NOT FOUND")
