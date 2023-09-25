for t in range(int(input())):
    a = {}
    m = 0
    ans = 1001
    for i in range(int(input())):
        x = int(input())
        if x in a:
            a[x] += 1
        else:
            a[x] = 1
        m = max(m, a[x])
    for i in a.keys():
        if a[i] == m:
            ans = min(ans, i)
    print(ans)

