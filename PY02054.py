n, m = map(int , input().split())
a = []
for _ in range(n):
    a.append(list(map(int, input().split())))
if n > m:
    k = n - m
    i = 1
    while k > 0:
        a.pop(i-1)
        i += 1
        k -= 1
else:
    for i in range(len(a)):
        j = 2
        k = m - n
        while k > 0:
            a[i].pop(j-1)
            j += 1
            k -= 1
for i in a:
    print(*i)